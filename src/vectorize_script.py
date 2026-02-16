from dotenv import load_dotenv
import os
from vectorize_book import vectorize_book_and_store_to_db , vectorize_chapters

load_dotenv()

class_subject_name = os.getenv("CLASS_SUBJECT_NAME")

vectorize_book_and_store_to_db(class_subject_name, vector_db_name="class_12_biology_vector_db")

vectorize_chapters(class_subject_name)

