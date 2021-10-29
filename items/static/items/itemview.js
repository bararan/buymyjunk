const imageForms = document.getElementsByClassName('multiField')
const uploadFields = document.getElementsByClassName('clearablefileinput')

window.onload = (e) => {
    last = 0
    while (true) {
        let imgField = imageForms[last]
        last++
        if (imgField.querySelectorAll('a').length == 0) {
            break
        }
    }   
    for(i=last;i<imageForms.length;i++) {
        imgField = imageForms[i]
        imgField.classList.add('hidden')
    }
    uploadFields.forEach((field, index) => {
        if (index< imageForms.length-1) {
            field.addEventListener('change', (e)=> {
                console.log('Changed ' + index)
                imageForms[index+1].classList.remove('hidden')
            })
        }
    })
}

$('.checkboxinput').on('change', function() {
    $('.checkboxinput').not(this).prop('checked', false);
 });

 $(document).on('click', '.confirm-delete', ()=> {
     return confirm('Are you sure you want to delete this item?');
 })


 function unhideNext(i) {
     imageForms[i+1].classList.remove('hidden')
 }