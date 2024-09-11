document.addEventListener("DOMContentLoaded", function() {
  // Fungsi untuk menyesuaikan tinggi textarea
  function adjustTextareaHeight(textarea) {
      textarea.style.height = "auto";  // Reset tinggi ke auto
      textarea.style.height = textarea.scrollHeight + "px";  // Atur tinggi sesuai scrollHeight
  }

  // Dapatkan semua textarea dan tambahkan event listener
  document.querySelectorAll("textarea").forEach(function (textarea) {
      // Menyesuaikan tinggi saat halaman dimuat
      adjustTextareaHeight(textarea);

      // Menyesuaikan tinggi saat pengguna mengetik
      textarea.addEventListener("input", function () {
          adjustTextareaHeight(textarea);
      });
  });
});