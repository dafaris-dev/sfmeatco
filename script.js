(function(){
  // Load splash
  requestAnimationFrame(function(){ document.body.classList.add('loaded'); });

  // Sticky nav state
  var nav = document.getElementById('nav');
  if(nav){
    var onScroll = function(){ nav.classList.toggle('is-stuck', window.scrollY > 24); };
    onScroll();
    window.addEventListener('scroll', onScroll, {passive:true});
  }

  // Mobile menu
  var btn = document.getElementById('menuBtn');
  var sheet = document.querySelector('.mobile-sheet');
  if(btn && sheet){
    btn.addEventListener('click', function(){
      document.body.classList.toggle('menu-open');
      var open = document.body.classList.contains('menu-open');
      btn.setAttribute('aria-expanded', open ? 'true':'false');
      sheet.setAttribute('aria-hidden', open ? 'false':'true');
    });
    sheet.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){ document.body.classList.remove('menu-open'); });
    });
  }

  // Reveal on scroll
  if('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, {rootMargin:'0px 0px -8% 0px', threshold:0.08});
    document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function(el){ el.classList.add('in'); });
  }

  // Current year
  var y = document.getElementById('yr');
  if(y){ y.textContent = String(new Date().getFullYear()); }

  // "Open today" badge on Visit page
  var todayEl = document.getElementById('todayHours');
  if(todayEl){
    var hoursByDay = {
      0: '11:00 am — 06:00 pm',
      1: null,
      2: '10:00 am — 07:00 pm',
      3: '10:00 am — 07:00 pm',
      4: '10:00 am — 07:00 pm',
      5: '10:00 am — 07:00 pm',
      6: '10:00 am — 07:00 pm'
    };
    var d = new Date();
    var h = hoursByDay[d.getDay()];
    var container = todayEl.closest('.vp-hours') || todayEl.closest('.hours-today');
    if(h){
      todayEl.textContent = h;
    } else {
      todayEl.textContent = 'Closed today';
      if(container){ container.classList.add('closed-today', 'closed'); }
      var strong = container && container.querySelector('strong');
      if(strong){ strong.textContent = 'Closed'; }
    }
  }

  // Mark active nav link by current page
  var path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a[data-page], .mobile-sheet a[data-page]').forEach(function(a){
    if(a.getAttribute('data-page') === path){ a.classList.add('active'); }
  });

  // Smooth anchor offset for in-page hashes only
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click', function(e){
      var id = a.getAttribute('href');
      if(id.length>1){
        var t = document.querySelector(id);
        if(t){
          e.preventDefault();
          var top = t.getBoundingClientRect().top + window.scrollY - 72;
          window.scrollTo({top:top, behavior:'smooth'});
        }
      }
    });
  });
})();
