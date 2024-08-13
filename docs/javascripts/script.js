const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in-up--active');
        } else {
            entry.target.classList.remove('fade-in-up--active');
        }
    });
});
  
const fade_in_ups = document.querySelectorAll('.fade-in-up');
fade_in_ups.forEach( fade_in_up => {
    observer.observe(fade_in_up);
});
