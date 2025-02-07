# ============================================================================================
#   Class Capacitor Bank
# ============================================================================================

class CapacitorBank:
    def __init__(self):
        self.bank_id = 0       # Capacitor Bank ID
        self.bus = 0           # Bus number where the capacitor bank is connected
        self.q = 0.0           # Reactive power rating (MVAr)
        self.n_steps            # nº of steps
        self.n_init             #initial tap position
        self.status = True      # Status: True if in service, False if out of service