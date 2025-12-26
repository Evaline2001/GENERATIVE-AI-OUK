walker init_user {
    has username: str;
    has useremail: str;

    start {
        user = User(name=username, email=useremail);
        here ++> user;
        report "User initialized.";
    }
}
