// 알라딘 API 키 저장 함수
function saveAladdinKey(key) {
    localStorage.setItem('ttbpopi07062229011', key);
}

// 국립중앙도서관 API 키 저장 함수
function saveNLKey(key) {
    localStorage.setItem('7653265afb3c171c6e4cab42edd95c435fe5e93ddfed4297fb7bb5db25641296', key);
}

// API 키 입력창 event listener (입력할 때마다 자동 저장)
document.getElementById('aladdinApiKeyInput')?.addEventListener('change', (e) => {
    saveAladdinKey(e.target.value);
});
document.getElementById('nlApiKeyInput')?.addEventListener('change', (e) => {
    saveNLKey(e.target.value);
});
