import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Простая база данных курсов криптовалют на основе словаря

crypto_rates = {
    'Bitcoin': {
        '2021': {'January': 32000, 'February': 33000, 'March': 34000, 'April': 35000, 'May': 36000, 'June': 37000,
                 'July': 38000, 'August': 39000, 'September': 40000, 'October': 41000, 'November': 42000,
                 'December': 43000},
        '2022': {'January': 44000, 'February': 45000, 'March': 46000, 'April': 47000, 'May': 48000, 'June': 49000,
                 'July': 50000, 'August': 51000, 'September': 52000, 'October': 53000, 'November': 54000,
                 'December': 55000},
        '2023': {'January': 56000, 'February': 57000, 'March': 58000, 'April': 59000, 'May': 60000, 'June': 61000,
                 'July': 62000, 'August': 63000, 'September': 64000, 'October': 65000, 'November': 66000,
                 'December': 67000},
        '2024': {'January': 68000, 'February': 69000, 'March': 70000, 'April': 71000, 'May': 72000, 'June': 73000,
                 'July': 74000, 'August': 75000, 'September': 76000, 'October': 77000, 'November': 78000,
                 'December': 79000}
    },
    'Ethereum': {
        '2021': {'January': 2200, 'February': 2300, 'March': 2400, 'April': 2500, 'May': 2600, 'June': 2700,
                 'July': 2800, 'August': 2900, 'September': 3000, 'October': 3100, 'November': 3200,
                 'December': 3300},
        '2022': {'January': 3400, 'February': 3500, 'March': 3600, 'April': 3700, 'May': 3800, 'June': 3900,
                 'July': 4000, 'August': 4100, 'September': 4200, 'October': 4300, 'November': 4400,
                 'December': 4500},
        '2023': {'January': 4600, 'February': 4700, 'March': 4800, 'April': 4900, 'May': 5000, 'June': 5100,
                 'July': 5200, 'August': 5300, 'September': 5400, 'October': 5500, 'November': 5600,
                 'December': 5700},
        '2024': {'January': 5800, 'February': 5900, 'March': 6000, 'April': 6100, 'May': 6200, 'June': 6300,
                 'July': 6400, 'August': 6500, 'September': 6600, 'October': 6700, 'November': 6800,
                 'December': 6900}
    },
    'Litecoin': {
        '2021': {'January': 160, 'February': 170, 'March': 180, 'April': 190, 'May': 200, 'June': 210,
                 'July': 220, 'August': 230, 'September': 240, 'October': 250, 'November': 260,
                 'December': 270},
        '2022': {'January': 280, 'February': 290, 'March': 300, 'April': 310, 'May': 320, 'June': 330,
                 'July': 340, 'August': 350, 'September': 360, 'October': 370, 'November': 380,
                 'December': 390},
        '2023': {'January': 400, 'February': 410, 'March': 420, 'April': 430, 'May': 440, 'June': 450,
                 'July': 460, 'August': 470, 'September': 480, 'October': 490, 'November': 500,
                 'December': 510},
        '2024': {'January': 520, 'February': 530, 'March': 540, 'April': 550, 'May': 560, 'June': 570,
                 'July': 580, 'August': 590, 'September': 600, 'October': 610, 'November': 620,
                 'December': 630}
    }
}

class CryptoConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер криптовалют")

        style = ttk.Style()  # Перемещаем определение style внутрь класса

        # Применяем стиль к кнопкам
        style.configure('TButton', font=('Arial', 12), background='lightblue')

        # Применяем стиль к меткам
        style.configure('TLabel', font=('Arial', 12), foreground='darkblue')

        # Создание и расположение элементов интерфейса
        self.crypto_label = ttk.Label(root, text="Выберите криптовалюту:")
        self.crypto_label.config(font=("Helvetica", 14), foreground="green")
        self.crypto_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.crypto_combobox = ttk.Combobox(root, values=list(crypto_rates.keys()))
        self.crypto_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.amount_label = ttk.Label(root, text="Введите количество:")
        self.amount_label.config(font=("Helvetica", 14), foreground="red")
        self.amount_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        self.date_label = ttk.Label(root, text="Выберите дату (Месяц Год):")
        self.date_label.config(font=("Helvetica", 14), foreground="purple")
        self.date_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.date_combobox = ttk.Combobox(root, values=self.generate_date_list())
        self.date_combobox.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button = ttk.Button(root, text="Конвертировать", command=self.convert)
        self.convert_button.grid(row=3, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.config(font=("Helvetica", 16), foreground="black")
        self.result_label.grid(row=4, columnspan=2, padx=10, pady=10)

    def generate_date_list(self):
        date_list = []
        for year in range(2024, 2020, -1):
            for month in range(1, 13):
                date_list.append(datetime(year, month, 1).strftime("%B %Y"))
        return date_list

    def convert(self):
        crypto = self.crypto_combobox.get()
        amount = float(self.amount_entry.get())
        month, year = self.date_combobox.get().split()
        rate = crypto_rates.get(crypto, {}).get(year, {}).get(month, 0)  # Если данные отсутствуют, устанавливаем курс равным 0
        total_dollars = amount * rate
        self.result_label.config(text=f"Сумма в долларах: ${total_dollars:.2f}")

def main():
    root = tk.Tk()
    app = CryptoConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
