function logSubmit(event) {
    var name = document.getElementById("name").value;
    var lastname = document.getElementById("lastname").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var birthday = document.getElementById("birthday").value;
    var gender1 = document.getElementById("gender1");
    if (name != "" && lastname != "" && email != "" && password != "" && birthday != "") {
        console.log("Name: ", name);
        console.log("Lastname: ", lastname);
        console.log("Email: ", email);
        console.log("Password: ", password);
        console.log("Birthday: ", birthday);
        if (gender1.checked) {
            gender = "Male";
        } else {
            gender = "Female";
        }
        console.log("Gender: ", gender);
        alert(`Name: ${name} \nLastname: ${lastname} \nEmail: ${email} \nPassword: ${password} \nBirthday: ${birthday} \nGender: ${gender} \nYou will be redirected to the login page to log in.`);

    }
    else{
        alert(`Please use valid data`);
        event.preventDefault();
        }
}

const form = document.getElementById('contactForm');
form.addEventListener('submit', logSubmit);