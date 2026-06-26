document.addEventListener("DOMContentLoaded", () => {
  // 1. Scroll Reveal Animation
  const revealElements = document.querySelectorAll(".reveal-up");

  const revealOnScroll = () => {
    const windowHeight = window.innerHeight;
    const revealPoint = 50;

    revealElements.forEach((el) => {
      const elementTop = el.getBoundingClientRect().top;
      if (elementTop < windowHeight - revealPoint) {
        el.classList.add("active");
      }
    });
  };

  // Trigger once on load
  revealOnScroll();

  // 2. Navbar Scroll Effect
  const navbar = document.getElementById("navbar");

  const handleNavbar = () => {
    if (window.scrollY > 50) {
      navbar.classList.add("navbar-scrolled");
    } else {
      navbar.classList.remove("navbar-scrolled");
    }
  };

  // Listen to scroll events
  window.addEventListener("scroll", () => {
    revealOnScroll();
    handleNavbar();
  });

  // 3. Portfolio Filtering
  const filterBtns = document.querySelectorAll(".filter-btn");
  const portfolioItems = document.querySelectorAll(".portfolio-item");

  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      // Remove active class from all buttons
      filterBtns.forEach((b) => {
        b.classList.remove(
          "active",
          "bg-brand-neonBlue/10",
          "text-brand-neonBlue",
          "border-brand-neonBlue/30",
        );
        b.classList.add("bg-white/5", "text-slate-300", "border-white/10");
      });

      // Add active class to clicked button
      btn.classList.add(
        "active",
        "bg-brand-neonBlue/10",
        "text-brand-neonBlue",
        "border-brand-neonBlue/30",
      );
      btn.classList.remove("bg-white/5", "text-slate-300", "border-white/10");

      const filterValue = btn.getAttribute("data-filter");

      portfolioItems.forEach((item) => {
        // Reset animation properties manually for smooth reflow
        item.style.opacity = "0";
        item.style.transform = "scale(0.95)";

        setTimeout(() => {
          if (
            filterValue === "all" ||
            item.getAttribute("data-category") === filterValue
          ) {
            item.style.display = "block";

            // Small delay before fading in
            setTimeout(() => {
              item.style.opacity = "1";
              item.style.transform = "scale(1)";
              item.style.transition = "all 0.4s ease";
            }, 50);
          } else {
            item.style.display = "none";
          }
        }, 300); // Wait for fade out
      });
    });
  });

  // 4. Image Modal for Portfolio
  const modal = document.getElementById("image-modal");
  const modalImg = document.getElementById("modal-img");
  const modalContent = document.getElementById("modal-content");
  const closeBtn = document.getElementById("close-modal");

  if (modal && modalImg && modalContent && closeBtn) {
    const openModal = (imgSrc) => {
      modalImg.src = imgSrc;
      modal.classList.remove("hidden");
      modal.classList.add("flex");

      // Trigger reflow
      void modal.offsetWidth;

      modal.classList.remove("opacity-0");
      modalContent.classList.remove("scale-95");
      modalContent.classList.add("scale-100");

      // Prevent body scroll
      document.body.style.overflow = "hidden";
    };

    const closeModal = () => {
      modal.classList.add("opacity-0");
      modalContent.classList.remove("scale-100");
      modalContent.classList.add("scale-95");

      setTimeout(() => {
        modal.classList.add("hidden");
        modal.classList.remove("flex");
        modalImg.src = "";
        document.body.style.overflow = "";
      }, 300);
    };

    // Attach click event to portfolio items
    portfolioItems.forEach((item) => {
      item.addEventListener("click", () => {
        const imgSrc = item.querySelector("img").src;
        openModal(imgSrc);
      });
    });

    closeBtn.addEventListener("click", closeModal);

    // Close on click outside
    modal.addEventListener("click", (e) => {
      if (e.target === modal || e.target === modalContent) {
        closeModal();
      }
    });

    // Close on Escape key
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !modal.classList.contains("hidden")) {
        closeModal();
      }
    });
  }

  // 6. Custom Modern Cursor
  if (window.matchMedia("(pointer: fine)").matches) {
    const cursor = document.createElement("div");
    cursor.classList.add("custom-cursor");

    const cursorFollower = document.createElement("div");
    cursorFollower.classList.add("custom-cursor-follower");

    document.body.appendChild(cursor);
    document.body.appendChild(cursorFollower);

    document.addEventListener("mousemove", (e) => {
      cursor.style.left = e.clientX + "px";
      cursor.style.top = e.clientY + "px";

      // Add slight delay for follower
      setTimeout(() => {
        cursorFollower.style.left = e.clientX + "px";
        cursorFollower.style.top = e.clientY + "px";
      }, 50);
    });

    // Hover effects on interactive elements
    const interactiveElements = document.querySelectorAll(
      "a, button, [onclick], input, textarea, select, .portfolio-item img, .service-tab-btn",
    );

    interactiveElements.forEach((el) => {
      el.addEventListener("mouseenter", () => {
        cursor.classList.add("hover-active");
        cursorFollower.classList.add("hover-active");
      });
      el.addEventListener("mouseleave", () => {
        cursor.classList.remove("hover-active");
        cursorFollower.classList.remove("hover-active");
      });
    });
  }

  // 7. Animated Testimonials Logic
  const testimonialsData = [
    {
      quote:
        "Pemasangan ACP dan Neon Box sangat rapi. Tim AngkasaAdv benar-benar mengerti standar kualitas untuk perusahaan skala nasional. Fasad gedung kami kini jauh lebih megah.",
      name: "Budi Santoso",
      designation: "PT Global Industries",
      src: "https://images.unsplash.com/photo-1557053910-d9eadeed1c58?q=80&w=1887&auto=format&fit=crop",
    },
    {
      quote:
        "Neon fleksibel custom yang dipesan pengerjaannya sangat cepat dan warnanya stunning! Benar-benar menjadi daya tarik utama untuk spot foto pelanggan kami.",
      name: "Anita Wijaya",
      designation: "Owner Cafe Senada",
      src: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=1888&auto=format&fit=crop",
    },
    {
      quote:
        "Struktur Huruf Timbul LED di atas gedung sangat solid menahan angin berkat konstruksi besi berkualitas tinggi. Pengerjaan di lapangan memastikan K3 dipatuhi.",
      name: "Risman Hakim",
      designation: "Direktur Teknis",
      src: "https://images.unsplash.com/photo-1568602471122-7832951cc4c5?q=80&w=2070&auto=format&fit=crop",
    },
    {
      quote:
        "Saya terkesan oleh desain 3D yang sangat akurat sebelum eksekusi dimulai. Hasil akhir Signboard kami persis seperti apa yang dijanjikan, bahkan lebih elegan.",
      name: "Rina Maharani",
      designation: "Manager Marketing NexusWorks",
      src: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=1888&auto=format&fit=crop",
    },
  ];

  const imageStack = document.getElementById("testi-image-stack");
  const nameEl = document.getElementById("testi-name");
  const desigEl = document.getElementById("testi-designation");
  const quoteEl = document.getElementById("testi-quote");
  const nextBtn = document.getElementById("testi-next-btn");
  const prevBtn = document.getElementById("testi-prev-btn");

  if (imageStack && testimonialsData.length > 0) {
    let activeTesti = 0;
    const cards = [];

    // Initialize images
    testimonialsData.forEach((t, i) => {
      const card = document.createElement("div");
      card.className =
        "absolute inset-0 origin-bottom rounded-3xl overflow-hidden shadow-2xl transition-all duration-500 ease-in-out border border-white/10";
      const img = document.createElement("img");
      img.src = t.src;
      img.alt = t.name;
      img.className = "h-full w-full object-cover";
      img.onerror = () => {
        img.src = `https://placehold.co/500x500/1e293b/00f0ff?text=${t.name.charAt(0)}`;
      };
      card.appendChild(img);
      imageStack.appendChild(card);
      cards.push(card);
    });

    const updateTestimonials = () => {
      cards.forEach((card, i) => {
        const diff = i - activeTesti;
        const absDiff = Math.abs(diff);

        let rotation = Math.floor(Math.random() * 16) - 8;
        if (i === activeTesti) rotation = 0;
        else if (i < activeTesti) rotation = -10 - absDiff * 4;
        else rotation = 10 + absDiff * 4;

        const len = testimonialsData.length;

        if (i === activeTesti) {
          card.style.opacity = "1";
          card.style.transform = `scale(1) translateY(0) rotate(0deg)`;
          card.style.zIndex = len;
        } else {
          card.style.opacity = "0.3";
          card.style.transform = `scale(0.9) translateY(20px) rotate(${rotation}deg)`;
          card.style.zIndex = len - absDiff;
        }
      });

      // Animate Text
      const textContainer = document.getElementById("testi-text-container");
      textContainer.style.opacity = "0";
      textContainer.style.transform = "translateY(20px)";

      setTimeout(() => {
        nameEl.textContent = testimonialsData[activeTesti].name;
        desigEl.textContent = testimonialsData[activeTesti].designation;
        quoteEl.textContent = '"' + testimonialsData[activeTesti].quote + '"';

        textContainer.style.opacity = "1";
        textContainer.style.transform = "translateY(0)";
      }, 300);
    };

    updateTestimonials();

    let autoPlayInterval = setInterval(() => {
      activeTesti = (activeTesti + 1) % testimonialsData.length;
      updateTestimonials();
    }, 5000);

    const manualUpdate = (newIndex) => {
      clearInterval(autoPlayInterval);
      activeTesti = newIndex;
      updateTestimonials();
      autoPlayInterval = setInterval(() => {
        activeTesti = (activeTesti + 1) % testimonialsData.length;
        updateTestimonials();
      }, 5000);
    };

    nextBtn.addEventListener("click", () => {
      manualUpdate((activeTesti + 1) % testimonialsData.length);
    });

    prevBtn.addEventListener("click", () => {
      manualUpdate(
        (activeTesti - 1 + testimonialsData.length) % testimonialsData.length,
      );
    });
  }

  // 8. Product Gallery Interactive Swap
  const mainProductImg = document.getElementById("main-product-img");
  const thumbnailGallery = document.getElementById("thumbnail-gallery");

  if (mainProductImg && thumbnailGallery) {
    // Collect all thumbnails
    const thumbnails = thumbnailGallery.querySelectorAll("img");

    thumbnails.forEach((thumb) => {
      // The parent element of the img holds the border and clickable area
      const thumbContainer = thumb.closest(".aspect-square");

      if (thumbContainer) {
        thumbContainer.addEventListener("click", () => {
          // Fade effect
          mainProductImg.style.opacity = "0.5";

          setTimeout(() => {
            // Swap src
            mainProductImg.src = thumb.src;
            mainProductImg.style.opacity = "1";

            // Reset state of all thumbnails
            thumbnails.forEach((t) => {
              const c = t.closest(".aspect-square");
              if (c) {
                c.classList.remove("border-brand-neonBlue");
                c.classList.add("border-white/5");
                t.classList.add("opacity-70");
                t.classList.remove("opacity-100");
              }
            });

            // Activate clicked thumbnail
            thumbContainer.classList.remove("border-white/5");
            thumbContainer.classList.add("border-brand-neonBlue");
            thumb.classList.remove("opacity-70");
            thumb.classList.add("opacity-100");
          }, 200); // Wait for fade out
        });
      }
    });
  }

  // 9. Mobile Sidebar Logic
  const mobileMenuBtn = document.getElementById("mobile-menu-btn");
  const closeSidebarBtn = document.getElementById("close-sidebar-btn");
  const mobileSidebar = document.getElementById("mobile-sidebar");
  const mobileSidebarOverlay = document.getElementById(
    "mobile-sidebar-overlay",
  );
  const mobileNavLinks = document.querySelectorAll(".mobile-nav-link");

  if (mobileMenuBtn && mobileSidebar) {
    const openSidebar = () => {
      mobileSidebarOverlay.classList.remove("hidden");

      // trigger reflow
      void mobileSidebarOverlay.offsetWidth;

      mobileSidebarOverlay.classList.add("opacity-100");
      mobileSidebarOverlay.classList.remove("opacity-0");

      mobileSidebar.classList.remove("translate-x-full");
      document.body.style.overflow = "hidden"; // Prevent scrolling
    };

    const closeSidebarMobile = () => {
      mobileSidebar.classList.add("translate-x-full");
      mobileSidebarOverlay.classList.add("opacity-0");
      mobileSidebarOverlay.classList.remove("opacity-100");

      setTimeout(() => {
        mobileSidebarOverlay.classList.add("hidden");
        document.body.style.overflow = "";
      }, 300);
    };

    mobileMenuBtn.addEventListener("click", openSidebar);
    if (closeSidebarBtn)
      closeSidebarBtn.addEventListener("click", closeSidebarMobile);
    if (mobileSidebarOverlay)
      mobileSidebarOverlay.addEventListener("click", closeSidebarMobile);

    mobileNavLinks.forEach((link) => {
      link.addEventListener("click", closeSidebarMobile);
    });
  }
});
