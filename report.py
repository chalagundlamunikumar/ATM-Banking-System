from fpdf import FPDF
from datetime import datetime

BANK_NAME = "State Bank of India"
IFSC_CODE = "SBIML06171805N"
MANAGER_NAME = "Mr.Muni Kumar"
BRANCH_NAME = "Naidupeta Main Branch"

def export_to_pdf(account_name, account_number, balance, transactions):
    pdf = FPDF()
    pdf.add_page()

    # -------- BANK HEADER --------
    pdf.image("image.png", 10, 8, 25)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, BANK_NAME, ln=True, align="C")

    pdf.set_font("Arial", size=11)
    pdf.cell(0, 8, f"IFSC Code : {IFSC_CODE}", ln=True, align="C")
    pdf.cell(0, 8, f"Branch : {BRANCH_NAME}", ln=True, align="C")
    pdf.ln(8)

    # -------- ACCOUNT DETAILS --------
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Account Statement", ln=True)
    pdf.ln(4)

    pdf.set_font("Arial", size=11)
    pdf.cell(0, 8, f"Account Holder : {account_name}", ln=True)
    pdf.cell(0, 8, f"Account Number : {account_number}", ln=True)
    pdf.cell(0, 8, f"Statement Generated : {datetime.now()}", ln=True)
    pdf.ln(6)

    # -------- TRANSACTION HISTORY --------
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Transaction History", ln=True)
    pdf.ln(4)

    pdf.set_font("Arial", size=11)

    if not transactions:
        pdf.cell(0, 8, "No transactions available.", ln=True)
    else:
        for idx, t in enumerate(transactions, start=1):
            pdf.multi_cell(0, 8, f"{idx}. {t}")

    pdf.ln(6)

    # -------- FINAL BALANCE --------
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, f"Final Available Balance : Rs. {balance}", ln=True)


    # -------- MANAGER SIGNATURE --------
    pdf.ln(15)
    pdf.image("sign.png", 140, pdf.get_y(), 40)

    pdf.ln(18)
    pdf.set_font("Arial", size=11)
    pdf.cell(0, 8, f"Branch Manager : {MANAGER_NAME}", ln=True, align="R")

    pdf.ln(5)
    pdf.set_font("Arial", "I", 10)
    pdf.cell(0, 8, "This is a system generated bank statement.", ln=True, align="C")

    pdf.output("Account_Statement.pdf")
    print("✅ Account_Statement.pdf generated successfully")
