const profileForm = document.getElementById('profile-form')
const imageInput = document.getElementById('image-input')
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value
const bio = document.getElementById("id_bio").value
const imgUpload = document.getElementById("image-input")
const currentAvatar = document.getElementById("current-avatar")
const modal = document.getElementById("profileEditModal")

imgUpload.addEventListener('change', (e)=> {
    currentAvatar.src = URL.createObjectURL(imgUpload.files[0])
})


// profileForm.addEventListener('submit', (e) => {
//         e.preventDefault()
//         // console.log(bio)
//         // console.log(imgUpload)
//         const formData = new FormData()
//         formData.append('csrfmiddlewaretoken', csrfToken)
//         formData.append('bio', bio)
//         formData.append('avatar', currentAvatar.src)
//         $.ajax(
//             {
//                 type: 'POST',
//                 url: '/profiles/update/',
//                 data: formData,
//                 success: (response) => {
//                     modal.setAttribute('aria-hidden', 'true')
//                 },
//                 success: () => {
//                     console.log(formData.get('avatar'))
//                 },
//                 processData: false,
//                 contentType: false,
//             }
//         )
//     }

// )