const imageForms = document.getElementsByClassName('multiField')
const uploadFields = document.getElementsByClassName('clearablefileinput')

window.onload = (e) => {
    console.log('loaded')
    last = 0
    while (true) {
        let imgField = imageForms[last]
        last++
        if (imgField.querySelectorAll('a').length == 0) {
            console.log('Will hide as of ' + last)
            break
        }
    }   
    for(i=last;i<imageForms.length;i++) {
        console.log('Now hiding ' + i)
        imgField = imageForms[i]
        imgField.classList.add('hidden')
        // hiddenFields.push(imgField)
    }
    uploadFields.forEach((field, index) => {
        if (index< imageForms.length-1) {
            field.addEventListener('change', (e)=> {
                console.log('Changed ' + index)
                imageForms[index+1].classList.remove('hidden')
            })
        }
    })
        // uploadField = document.getElementById("id_form-"+i+"-image")
}

$('input:checkbox').on('change', function() {
    $('input:checkbox').not(this).prop('checked', false);
 });

 $(document).on('click', '.confirm-delete', ()=> {
     return confirm('Are you sure you want to delete this item?');
 })


 function unhideNext(i) {
     imageForms[i+1].classList.remove('hidden')
 }
 
 