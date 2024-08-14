const ioConfiguration = {
    rootMargin: '-200px 0% -200px 0%',
    threshold: 0
  };

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
}, ioConfiguration);

const intersects = document.querySelectorAll('[class*="intersect"]');
intersects.forEach( intersect => {
    observer.observe(intersect);
});
