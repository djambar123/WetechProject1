class LoginLocators:

    # LoginPage elements
    email_txtbox_name = "//input[@placeholder='Email']"
    pass_txtbox_name = "//input[@placeholder='Password']"
    login_btn_name = "//button[@class='loginButton']"

    # HomePage elements
    login_page_xpath = "(//button[normalize-space()='Log into Account'])[1]"
    logout_link_xpath = "//a[@href='http://themiscode.com/panel/General/logout']"
    user_partial_link_text = "Welcome dear"
    lawsuit_link_xpath = "//a[@href='http://themiscode.com/panel/Lawsuit/index']"

    # LawsuitPage elements

    # List records
    data_records_dropbox_name = "DataTables_Table_0_length"

    # Find case files elements
    filter_case_state_dropbox_name = "state"
    filter_case_client_txtbox_name = "client"
    filter_file_no_txtbox_name = "foy_no"
    filter_defendant_txtbox_name = "defendant"
    filter_case_type_dropbox_name = "case_type"
    filter_search_btn_name = "search"
    filtered_search_result_sheet_no_xpath = "//a[contains(text(),'9000')]"