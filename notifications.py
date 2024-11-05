# notifications.py

def send_email(to_email, subject, content):
    print(f"[SIMULAZIONE EMAIL] Invio email a: {to_email}")
    print(f"Soggetto: {subject}")
    print(f"Contenuto:\n{content}\n")
    print("Email inviata con successo (simulato)")

def send_sms(to_number, message):
    print(f"[SIMULAZIONE SMS] Invio SMS a: {to_number}")
    print(f"Messaggio: {message}")
    print("SMS inviato con successo (simulato)")

if __name__ == "__main__":
    send_email("test@example.com", "Conferma Ordine", "<p>Il tuo ordine è stato confermato!</p>")
    send_sms("+123456789", "Il tuo ordine è stato confermato!")
