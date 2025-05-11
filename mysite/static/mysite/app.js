
    // Secure function to animate numbers
    function animateNumbers() {
      // Retrieve the DOM elements
      const vehicleElement = document.getElementById('vehicles');
      const driverElement = document.getElementById('drivers');
      const expenseElement = document.getElementById('expenses');
      const waybillElement = document.getElementById('waybills');

      // Function to animate a number
      const animate = (element, target, duration) => {
        let start = 0;
        const step = target / duration;
        const interval = setInterval(() => {
          start += step;
          if (start >= target) {
            start = target;
            clearInterval(interval);
          }
          element.innerHTML = target === 1245000 ? '₵' + start.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g, ',') : start.toFixed(0);
        }, 1);
      };

      // Animate all values with smooth transitions
      animate(vehicleElement, parseInt(vehicleElement.innerText), 1000);
      animate(driverElement, parseInt(driverElement.innerText), 1000);
      animate(expenseElement, parseInt(expenseElement.innerText), 1000);
      animate(waybillElement, parseInt(waybillElement.innerText), 1000);
    }

    // Run the number animation when the page is fully loaded
    window.onload = animateNumbers;

