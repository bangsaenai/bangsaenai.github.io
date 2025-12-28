from http.server import BaseHTTPRequestHandler
import json
import numpy as np

# --- 🧠 SECRET SAUCE: พื้นที่ใส่ Koopman ของจริง ---
def solve_koopman_trajectory(L, C, steps=1000, dt=50e-6):
    # นี่คือที่ที่ท่านใส่ Code Python ของจริงที่ท่านมี
    # สมมติ Logic การคำนวณแบบ Matrix (Lifted Space)
    
    # Init System State x = [iL, vC]
    x = np.array([[0.0], [311.0]]) # Start at 311V
    
    # System Matrices (Example for VSI)
    # dx/dt = Ax + Bu
    A_sys = np.array([
        [0, -1/L],
        [1/C, -1/(C*100)] # Load 100 ohm initial
    ])
    B_sys = np.array([[1/L], [0]])
    
    # Koopman Gain (คำนวณจาก L, C ที่ส่งมา)
    # สมมติสูตรการหา K จาก Koopman Eigenfunctions
    K_gain = np.array([[L*10000, C*2000]]) # ตัวอย่าง Dummy Gain
    
    time_data = []
    pid_data = [] # สมมติว่ามี Simulation PID เทียบด้วย
    kks_data = []
    
    # Simulation Loop
    for i in range(steps):
        t = i * dt
        
        # Scenario: Load Change at 25ms (100 -> 10 ohm)
        R_load = 10.0 if t > 0.025 else 100.0
        
        # Update Plant Dynamics based on R
        A_sys[1,1] = -1/(C*R_load)
        
        # --- KKS Control Law (Hidden Logic) ---
        # u = -K * Psi(x)  <-- นี่คือ Lifted Space Logic
        u_kks = 311.0 - (K_gain @ (x - np.array([[0], [311.0]])))[0,0]
        u_kks = np.clip(u_kks, 0, 400) # Saturation
        
        # Euler Integration (Physics)
        dx = (A_sys @ x) + (B_sys * u_kks)
        x = x + dx * dt
        
        # Store Data
        time_data.append(round(t*1000, 2))
        kks_data.append(float(x[1,0]))
        
        # (ทำ PID Simulation ควบคู่กันไปเพื่อเปรียบเทียบ...)
        # pid_data.append(...) 
        
    return {
        "time": time_data,
        "kks": kks_data,
        "pid": [311.0]*steps # ใส่ค่า PID จริงของท่านตรงนี้
    }

# --- Vercel Handler (ตัวรับส่งข้อมูล) ---
class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len)
        data = json.loads(body)
        
        L = float(data.get('L', 2.5e-3)) # รับค่าจากหน้าเว็บ
        C = float(data.get('C', 50e-6))
        
        # เรียกฟังก์ชันคำนวณลับ
        result = solve_koopman_trajectory(L, C)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))
