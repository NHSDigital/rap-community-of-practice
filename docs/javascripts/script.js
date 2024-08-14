const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        let entryClasses = Array.from(entry.target.classList.values())
        let intersects = entryClasses.filter(class_ => class_.includes("intersect") );
        if (entry.isIntersecting) {
            intersects.forEach((intersect_class) => {
                entry.target.classList.add(intersect_class + '--active');
            })
        } else {
            intersects.forEach((intersect_class) => {
                entry.target.classList.remove(intersect_class + '--active');
            })
        }
    });
});
  
const fade_in_ups = document.querySelectorAll('.intersect-fade-in-up');
fade_in_ups.forEach( fade_in_up => {
    observer.observe(fade_in_up);
});
