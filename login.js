const email = document.getElementById('email')
const password = document.getElementById('password')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')

form.addEventListener('submit', (e) => {
    let messages = []
    if (email.value === '' || email.value == null) {
        messages.push('**Your Email is required')
        email.style.border = '1px solid #F80F0F'
    }

    if (password.value.length < 6){
        messages.push('**Password must be longer than 6 characters')
        password.style.border = '1px solid #F80F0F'
    }

    if (password.value.length >= 15) {
        messages.push('**Password must be less than 15 characters')
        password.style.border = '1px solid #F80F0F'
    }

    if (password.value === 'password') {
        messages.push('**Password cannot be password')
        password.style.border = '1px solid #F80F0F'
    }

    if (messages.length > 0) {
        e.preventDefault()
        errorElement.innerText = messages.join(' \n ')
    }
})