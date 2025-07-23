/* Very small AJAX helper for the contact form */
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contactForm');
  const submitBtn = document.getElementById('submitBtn');
  const resultBox = document.getElementById('formResult');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    toggleLoading(true);

    const formData = new FormData(form);
    try {
      const res = await fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
      });

      const data = await res.json();
      console.log(data);

      if (res.ok) {
        resultBox.textContent = data.message || 'Thanks! We will get back to you shortly.';
        form.reset();
      } else {
        resultBox.textContent = data.error || 'Something went wrong.';
      }
    } catch (err) {
      resultBox.textContent = 'Network error. Please try again.';
    } finally {
      toggleLoading(false);
    }
  });

  function toggleLoading(state) {
    submitBtn.disabled = state;
    submitBtn.querySelector('.text').style.display = state ? 'none' : 'inline';
    submitBtn.querySelector('.spinner').style.display = state ? 'inline-block' : 'none';
  }
});