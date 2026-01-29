class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.ratings = []

    def add_rating(self, rate):
        self.ratings.append(rate)

    def average_reting(self):
        if not self.ratings:
            return "Baholanmagan!"
        return sum(self.ratings) / len(self.ratings)

    def get_info(self):
        return f"Shifokor: {self.name}, Mutaxassisligi: {self.specialty}, Reytingi: {self.average_reting()}"


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Bemorning ismi: {self.name}, Bemorning yoshi: {self.age}"


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.records = {}
        self.doctor_schedule = {}

    # yangi shifokor qo‘shish
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        self.doctor_schedule[doctor.name] = []

    # yangi bemor qo‘shish
    def add_patient(self, patient):
        self.patients.append(patient)
        self.records[patient.name] = []

    # qabulga yozish
    def book(self, patient, doctor, time):
        if time in self.doctor_schedule[doctor.name]:
            print("Doktor bu vaqtda band, boshqa vaqt tanlang!")
            return

        self.doctor_schedule[doctor.name].append(time)
        self.records[patient.name].append((doctor.name, time))
        print(f"{patient.name} {doctor.name} ga {time} vaqtiga yozildi.")

    # qabulni bekor qilish
    def cancel(self, patient, doctor, time):
        if (doctor.name, time) in self.records[patient.name]:
            self.records[patient.name].remove((doctor.name, time))
            self.doctor_schedule[doctor.name].remove(time)
            print("Qabul muvaffaqiyatli bekor qilindi!")
        else:
            print("Bunday yozuv topilmadi.")

    # shifokor band vaqtlarini ko‘rsatish
    def get_doctor_schedule(self, doctor):
        times = self.doctor_schedule[doctor.name]
        if not times:
            print(f"{doctor.name} hozircha bo‘sh.")
        else:
            print(f"{doctor.name} band vaqtlari:", times)

    # bemorning barcha qabul vaqtlari
    def get_patient_appointments(self, patient):
        apps = self.records[patient.name]
        if not apps:
            print(f"{patient.name} ning qabullari yo‘q.")
        else:
            print(f"{patient.name} ning qabullari:", apps)


# ==== TEST QISMI ====

d1 = Doctor("Aliyev M", "Kardiolog")
d2 = Doctor("Karimovna Sh", "Tish shifokori")

p1 = Patient("Muhammad", 20)
p2 = Patient("Bilol", 12)

hospital = Hospital("Toshkent Markaziy Shifoxona")

hospital.add_doctor(d1)
hospital.add_doctor(d2)

hospital.add_patient(p1)
hospital.add_patient(p2)

hospital.book(p1, d1, "10:00")
hospital.book(p2, d1, "10:00")  # band vaqt
hospital.book(p2, d1, "11:00")

hospital.get_doctor_schedule(d1)
hospital.get_patient_appointments(p1)

hospital.cancel(p1, d1, "10:00")
hospital.get_doctor_schedule(d1)
