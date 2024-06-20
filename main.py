

def main():
    path_to_file = 'books/frankenstein.txt'

    with open(path_to_file) as f:
        file_contents = f.read()
    words = file_contents.split()
    print(f'--- Begin report of {path_to_file} ---')
    print(f'{len(words)} words found in the document')
    print('\n')
    
    letter_dict = {}
    for word in words:
        lowered_word = word.lower()
        for letter in lowered_word:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    report_list = []
    for key, value in letter_dict.items():
        if key.isalpha():
            report_dict = {"letter" : key, "count": value} 
        else:
            continue
        report_list.append(report_dict)

    def sort_on_count(dict):
        return dict["count"]
    
    report_list.sort(reverse=True, key=sort_on_count)

    for report in report_list:
        print(f'The \'{report["letter"]}\' character was found {report["count"]} times')

    print("--- End report ---")

if __name__ == "__main__":
    main()
