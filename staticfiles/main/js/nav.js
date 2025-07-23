(function () {
  const toggle = document.getElementById('navToggle');
  const nav    = document.getElementById('navLinks');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', () => {
    nav.classList.toggle('open');
  });
})();