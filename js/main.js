const header = document.getElementById('siteHeader');
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const estimateForm = document.getElementById('estimateForm');
const formNote = document.getElementById('formNote');

function updateHeader() {
  header.classList.toggle('is-scrolled', window.scrollY > 24);
}

function toggleMenu() {
  const isOpen = navMenu.classList.toggle('is-open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
}

function closeMenu(event) {
  if (event.target.tagName === 'A') {
    navMenu.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', 'false');
  }
}

function handleEstimateSubmit(event) {
  event.preventDefault();
  formNote.textContent = 'Thanks. This draft form is ready to connect to GHL/n8n before publishing.';
  estimateForm.reset();
}

document.addEventListener('DOMContentLoaded', updateHeader);
window.addEventListener('scroll', updateHeader, { passive: true });
if (navToggle && navMenu) {
  navToggle.addEventListener('click', toggleMenu);
  navMenu.addEventListener('click', closeMenu);
}
if (estimateForm && formNote) {
  estimateForm.addEventListener('submit', handleEstimateSubmit);
}
