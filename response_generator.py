from database import fetch_api_info
import random

def generate_response(intent):
  if intent == "greeting":
    responses = [
      "Halo, selamat datang di Chatbot API bank bjb. Ada yang bisa saya bantu?",
      "Hai, selamat datang di Chatbot API bank bjb.",
      "Halo! Ada yang bisa saya bantu?",
      "Halo! Apa yang bisa saya lakukan untukmu?",
      "Hi! Butuh bantuan dengan sesuatu?"
    ]
    return random.choice(responses)
  elif intent == "goodbye":
    responses = [
      "Jika butuh bantuan dengan hal lain, jangan ragu untuk bertanya. Terima kasih, sampai jumpa!"
    ]
    return random.choice(responses)
  elif intent == "requirement":
    api_data = fetch_api_info("requirement")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "inquiry_balance":
    api_data = fetch_api_info("inquiry_balance")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "request_headers":
    api_data = fetch_api_info("request_headers")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "signature_format":
    api_data = fetch_api_info("signature_format")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "transaction_history":
    api_data = fetch_api_info("transaction_history")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "account_internal":
    api_data = fetch_api_info("account_internal")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "account_external":
    api_data = fetch_api_info("account_external")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "overbooking":
    api_data = fetch_api_info("overbooking")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "transfer_online":
    api_data = fetch_api_info("transfer_online")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "card_registration":
    api_data = fetch_api_info("card_registration")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "payment":
    api_data = fetch_api_info("payment")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  elif intent == "validate_otp":
    api_data = fetch_api_info("validate_otp")
    if api_data:
      return api_data['response']
    else:
      return "Maaf, API tidak ditemukan."
  else:
    return "Maaf, saya tidak mengerti. ketik ."