# order_manager.py
import random
import string
import time
from notifications import send_email, send_sms
from database import create_connection

def add_order(customer_name, product_name, quantity):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO orders (customer_name, product_name, quantity, status)
                      VALUES (?, ?, ?, ?)''',
                   (customer_name, product_name, quantity, "In elaborazione"))
    conn.commit()
    conn.close()
    
    print(f"Ordine aggiunto per {customer_name} - {product_name} x{quantity}")

def get_orders():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor .fetchall()
    conn.close()
    return orders
    
def update_order_status(order_id, new_status):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET status = ? WHERE id = ?", (new_status, order_id))
    conn.commit()
    conn.close()
    print(f"Stato dell'ordine {order_id} aggiornato a: {new_status}")

def generate_tracking_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def process_order_flow(order_id):
    # Simula il passaggio attraverso diversi stati
    status_sequence = ["In elaborazione", "Spedito", "Consegnato"]
    for status in status_sequence:
        if status == "Spedito":
            tracking_number = generate_tracking_number()
            update_order_tracking(order_id, tracking_number)  # Aggiungiamo la funzione di tracking
            send_email("cliente@example.com", f"Ordine {order_id} {status}", f"Il tuo ordine è stato spedito! Numero di tracking: {tracking_number}")
            send_sms("+123456789", f"Il tuo ordine {order_id} è stato spedito! Numero di tracking: {tracking_number}")
        elif status == "Consegnato":
            send_email("cliente@example.com", f"Ordine {order_id} {status}", f"Il tuo ordine è stato consegnato!")
            send_sms("+123456789", f"Il tuo ordine {order_id} è stato consegnato!")
        update_order_status(order_id, status)
        # Simula il tempo di attesa tra gli stati
        time.sleep(2)  # Aspetta 2 secondi per simulare il tempo di transizione

def update_order_tracking(order_id, tracking_number):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET tracking_number = ? WHERE id = ?", (tracking_number, order_id))
    conn.commit()
    conn.close()
    print(f"Numero di tracking dell'ordine {order_id} aggiornato a: {tracking_number}")

def simulate_tracking_update(order_id):
    # Simula aggiornamenti di tracking
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT tracking_number, status FROM orders WHERE id = ?", (order_id,))
    result = cursor.fetchone()
    conn.close()

    if result and result[1] == "Spedito":  # Verifica se è "Spedito" per procedere
        print(f"[SIMULAZIONE TRACKING] Verifica dello stato del tracking per ordine {order_id}")
        time.sleep(3)  # Simula tempo di attesa per un aggiornamento

        # Aggiorna lo stato a "Consegnato" come simulazione di completamento
        update_order_status(order_id, "Consegnato")
        send_email("cliente@example.com", f"Ordine {order_id} Consegnato", f"Il tuo ordine {order_id} è stato consegnato!")
        send_sms("+123456789", f"Il tuo ordine {order_id} è stato consegnato!")
        print(f"Ordine {order_id} consegnato (simulato).")

if __name__ == "__main__":
    add_order("Alice", "Smartphone", 1)
    process_order_flow(1)  # Simula l'avanzamento dell'ordine
    simulate_tracking_update(1)  # Simula il completamento del tracking
