// querySelector: 웹페이지의 요소를 가져오는 메소드

const targetForm = document.querySelector('.jss_content_form') // 입력창의 class값을 가져와 targetForm으로 지정
const counted_text = document.querySelector('.counted_text') // 글자수 표시 부분의 class값을 가져와 counted_text로 지정
targetForm.addEventListener("keyup", function() { // keyup이라는 이벤트가 발생시, function()실행
    counted_text.innerHTML = targetForm.value.length // counted_text의 내부 html값을 targetForm의 값 길이로 저장
})