function logSubmit(event) {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if (email != "" && password != "") {
        console.log("Email: ", email);
        console.log("Password: ", password);
        alert(`Email: ${email} \nPassword: ${password} \nIf your credentials are correct you will be redirected to the students page.`);

    }
    else{
        alert(`Please use valid data`);
        event.preventDefault();
        }
}

const form = document.getElementById('contactForm');
form.addEventListener('submit', logSubmit);