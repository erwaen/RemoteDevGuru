
# Takes a string input from the user and converts it to
# a boolean value.
def user_input_to_bool(prompt: str):
    user_input = input(prompt).lower()
    if user_input == 'y' or user_input == 'yes':
        return True
    else:
        return False

# This function accepts the default metadata generated by the JSONLoader
# extraction function from Langchain and allows us to modify the
# metadata to our convenience.
#
# This version is for the data extracted from LinkedIn.
def metadata_fun_linkedin(record: dict, metadata: dict) -> dict:
    metadata["source"] = record.get("url_detalle_trabajo")
    metadata["date_of_scrapping"] = record.get("fecha_de_scrapeo")
    metadata["job_title"] = record.get("titulo_del_trabajo")
    return metadata

# This version is for the data extracted from other websites.
def metadata_fun_web(record: dict, metadata: dict) -> dict:
    metadata["source"] = record.get("link")
    metadata["date_of_scrapping"] = record.get("scrape_date")
    metadata["article_title"] = record.get("title")
    return metadata
