function logout() {
  
    window.location.href = "login.html";
}


class FormValidator {
    constructor(formId, errorMsgId) {
        this.form = document.getElementById(formId);
        this.errorMsg = document.getElementById(errorMsgId);
    }

    validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email.trim() === '') {
            this.showError('Please enter your email.');
            return false;
        }
        if (!emailRegex.test(email)) {
            this.showError('Please enter a valid email address.');
            return false;
        }
        return true;
    }

    validatePassword(password) {
        const passRegex = /^(?=.*[A-Za-z])(?=.*\d).{8,}$/;
        if (password.trim() === '') {
            this.showError('Please enter your password.');
            return false;
        }
        if (!passRegex.test(password)) {
            this.showError('Password must be at least 8 characters long and include one letter and one number.');
            return false;
        }
        return true;
    }

    showError(message) {
        this.errorMsg.innerText = message;
    }
}

class SignupValidator extends FormValidator {
    validate() {
        const email = this.form.elements['email'].value;
        const pass1 = this.form.elements['pass1'].value;
        const pass2 = this.form.elements['pass2'].value;

        if (!this.validateEmail(email)) return;
        if (!this.validatePassword(pass1)) return;
        if (pass1 !== pass2) {
            this.showError('Passwords do not match.');
            return;
        }

        const userData = { email: email, password: pass1 };
        localStorage.setItem('userData', JSON.stringify(userData));
        alert('Signup successful! Redirecting to login page.');
        window.location.href = "login.html";
    }
}

class LoginValidator extends FormValidator {
    validate() {
        const email = this.form.elements['email'].value;
        const pass = this.form.elements['pass'].value;

        if (!this.validateEmail(email)) return;
        if (!this.validatePassword(pass)) return;

        const userDataJSON = localStorage.getItem('userData');
        if (!userDataJSON) {
            this.showError('User not found. Please sign up first.');
            return;
        }

        const userData = JSON.parse(userDataJSON);
        if (email !== userData.email || pass !== userData.password) {
            this.showError('Invalid email or password.');
            return;
        }
        alert('Login successful! Redirecting to home page.');
        window.location.href = "home.html";
    }
}
