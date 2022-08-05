const email = document.getElementById('email')
const password = document.getElementById('password')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')

form.addEventListener('submit', (e) => {
    let messages = []
    if (email.value === '' || email.value == null) {
        messages.push('Please your Email is required')
    }

    if (password.value.length < 6){
        messages.push('Password must be longer than 6 characters')
    }

    if (password.value.length > 10){
        messages.push('Password must be less than 10 characters')
    }

    if (password.value === 'password'){
        messages.push('Password cannot be password')
    }

    if (messages.length > 0) {
        e.preventDefault()
        errorElement.innerText = messages.join(', ')
    }
})