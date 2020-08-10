const inputImage = document.getElementById('id_image')
const imageContainer = document.querySelector('.image-change')
const imageTitle = document.querySelector('.add-image')
const imagePreview = document.querySelector('.img-preview')
const closeButton = document.querySelector('.close')
const form = document.getElementById('form')

inputImage.addEventListener('change', function () {
    const file = this.files[0]

    if (file) {
        const reader = new FileReader()

        imageTitle.style.display = 'none'
        imageContainer.style.display = 'block'

        reader.addEventListener('load', function () {
            imagePreview.setAttribute('src', this.result)
            document.querySelector('#id_image').value = this.result
        })
        reader.readAsDataURL(file)
    }
})

closeButton.addEventListener('click', function () {
    imagePreview.setAttribute('src', null)
    imageContainer.style.display = 'none'
    imageTitle.style.display = 'block'
    document.querySelector('#id_image').value = ''
})
