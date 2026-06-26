import os

portfolio_html = """
    <!-- Portfolio Section -->
    <section id="portfolio" class="py-24 relative bg-brand-dark overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6 reveal-up">
                <div class="max-w-2xl">
                    <h2 class="text-brand-neonBlue font-semibold uppercase tracking-wider text-sm mb-3">Karya Pilihan</h2>
                    <h3 class="text-4xl font-heading font-bold text-white">Project Terbaru Kami</h3>
                </div>
                <!-- Categories filter -->
                <div class="flex gap-2 flex-wrap">
                    <button class="px-5 py-2 rounded-full bg-brand-neonBlue/10 text-brand-neonBlue border border-brand-neonBlue/30 text-sm font-medium transition-colors filter-btn active" data-filter="all">Semua</button>
                    <button class="px-5 py-2 rounded-full bg-white/5 text-slate-300 border border-white/10 hover:bg-white/10 text-sm font-medium transition-colors filter-btn" data-filter="kantor">Kantor</button>
                    <button class="px-5 py-2 rounded-full bg-white/5 text-slate-300 border border-white/10 hover:bg-white/10 text-sm font-medium transition-colors filter-btn" data-filter="cafe">Café/Resto</button>
                    <button class="px-5 py-2 rounded-full bg-white/5 text-slate-300 border border-white/10 hover:bg-white/10 text-sm font-medium transition-colors filter-btn" data-filter="ruko">Ruko</button>
                </div>
            </div>

            <!-- Custom grid for portfolio -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="portfolio-grid">
                
                <!-- Item 1 - Huruf Timbul Kantor -->
                <div class="reveal-up portfolio-item rounded-2xl overflow-hidden group cursor-pointer relative" data-category="kantor">
                    <div class="aspect-[4/3] bg-brand-card overflow-hidden relative">
                        <img src="img/portfolio-huruf-timbul.png" alt="Huruf Timbul Kantor" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent flex flex-col justify-end p-6">
                            <span class="px-3 py-1 bg-brand-neonBlue/20 border border-brand-neonBlue/30 rounded-full text-xs text-brand-neonBlue mb-3 inline-block w-max">Kantor</span>
                            <h4 class="text-xl font-heading font-bold text-white mb-1 group-hover:text-brand-neonBlue transition-colors">Huruf Timbul LED "ANGKASA"</h4>
                            <p class="text-slate-300 text-sm mb-4">Industrial finish, Backlit LED</p>
                        </div>
                    </div>
                </div>

                <!-- Item 2 - Neon Box Cafe -->
                <div class="reveal-up portfolio-item rounded-2xl overflow-hidden group cursor-pointer relative" data-category="cafe" style="transition-delay: 100ms;">
                    <div class="aspect-[4/3] bg-brand-card overflow-hidden relative">
                        <img src="img/portfolio-neon-box.png" alt="Neon Box Cafe" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent flex flex-col justify-end p-6">
                            <span class="px-3 py-1 bg-brand-neonPink/20 border border-brand-neonPink/30 rounded-full text-xs text-brand-neonPink mb-3 inline-block w-max">Café/Resto</span>
                            <h4 class="text-xl font-heading font-bold text-white mb-1 group-hover:text-brand-neonPink transition-colors">Neon Box "Warung Kita"</h4>
                            <p class="text-slate-300 text-sm mb-4">Warm neon glow, Acrylic panel</p>
                        </div>
                    </div>
                </div>

                <!-- Item 3 - Branding Ruko Before/After -->
                <div class="reveal-up portfolio-item rounded-2xl overflow-hidden group cursor-pointer relative lg:row-span-2" data-category="ruko" style="transition-delay: 200ms;">
                    <div class="h-full min-h-[400px] bg-brand-card overflow-hidden relative">
                        <img src="img/portfolio-branding-ruko.png" alt="Branding Ruko" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-black/10"></div>
                        <div class="absolute bottom-0 left-0 p-8 w-full">
                            <span class="px-3 py-1 bg-brand-neonBlue/20 border border-brand-neonBlue/30 rounded-full text-xs text-brand-neonBlue mb-4 inline-block font-semibold">Transformasi Total</span>
                            <h4 class="text-2xl font-heading font-bold text-white mb-2 group-hover:text-brand-neonBlue transition-colors">Fasad Gadget Jaya</h4>
                            <p class="text-slate-300 text-sm mb-4">Before-After perombakan total fasad ruko dengan kombinasi neon panel dan arsitektural lighting.</p>
                            <div class="flex items-center gap-2 text-xs font-semibold text-brand-neonBlue opacity-0 group-hover:opacity-100 transition-opacity mt-4">
                                <i class="ri-zoom-in-line text-lg"></i> Klik untuk memperbesar visual
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Item 4 - Signboard Office -->
                <div class="reveal-up portfolio-item rounded-2xl overflow-hidden group cursor-pointer relative" data-category="kantor" style="transition-delay: 300ms;">
                    <div class="aspect-[4/3] bg-brand-card overflow-hidden relative">
                        <img src="img/portfolio-signboard.png" alt="Signboard Office" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent flex flex-col justify-end p-6">
                            <span class="px-3 py-1 bg-white/10 border border-white/20 rounded-full text-xs text-white mb-3 inline-block w-max backdrop-blur-md">Kantor</span>
                            <h4 class="text-xl font-heading font-bold text-white mb-1 group-hover:text-brand-neonBlue transition-colors">Corporate Sign "PT Teknologi"</h4>
                            <p class="text-slate-300 text-sm mb-4">Minimalist white LED, Solid concrete wall</p>
                        </div>
                    </div>
                </div>

                <!-- Item 5 - Neon Flex Art -->
                <div class="reveal-up portfolio-item rounded-2xl overflow-hidden group cursor-pointer relative" data-category="cafe" style="transition-delay: 400ms;">
                    <div class="aspect-[4/3] bg-brand-card overflow-hidden relative">
                        <img src="img/portfolio-neon-flex.png" alt="Neon Flex Art" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent flex flex-col justify-end p-6">
                            <span class="px-3 py-1 bg-brand-neonPink/20 border border-brand-neonPink/30 rounded-full text-xs text-brand-neonPink mb-3 inline-block w-max">Ruko / Venue</span>
                            <h4 class="text-xl font-heading font-bold text-white mb-1 group-hover:text-brand-neonPink transition-colors">Neon Flex Art "Galeri Seni"</h4>
                            <p class="text-slate-300 text-sm mb-4">Artistic signage with vivid pink & cyan</p>
                        </div>
                    </div>
                </div>

            </div>

            <div class="text-center mt-16 reveal-up">
                <a href="#contact" class="inline-flex items-center gap-2 text-slate-400 hover:text-white transition-colors cursor-pointer text-sm font-medium">
                    Punya ide desain sendiri? Diskusikan dengan tim spesialis kami <i class="ri-arrow-right-line"></i>
                </a>
            </div>
        </div>
    </section>
"""

contact_html = """
    <!-- Call To Action & Contact -->
    <section id="contact" class="py-24 relative bg-[#060B18]">
        <div class="absolute inset-0 z-0">
            <!-- Grid pattern -->
            <div class="w-full h-full opacity-[0.03]" style="background-image: radial-gradient(circle at center, #ffffff 1px, transparent 1px); background-size: 32px 32px;"></div>
            <div class="absolute right-0 bottom-0 w-[500px] h-[500px] bg-brand-neonBlue/10 rounded-full blur-[100px] pointer-events-none"></div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="bg-brand-card rounded-3xl border border-white/5 overflow-hidden flex flex-col lg:flex-row reveal-up">
                <!-- Left info -->
                <div class="lg:w-5/12 p-10 md:p-16 flex flex-col justify-between relative bg-gradient-to-br from-brand-card to-[#0A1021]">
                    <div class="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-brand-neonBlue to-blue-600"></div>
                    <div>
                        <h3 class="text-3xl font-heading font-bold text-white mb-4">Siap Membuat Bisnis Anda Lebih Terlihat?</h3>
                        <p class="text-slate-400 text-sm leading-relaxed mb-8">
                            Konsultasikan kebutuhan advertising Anda secara gratis. Kami siap memberikan solusi desain, material, hingga penawaran harga terbaik untuk area Jabodetabek.
                        </p>

                        <div class="space-y-6">
                            <div class="flex items-start gap-4">
                                <div class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center shrink-0 text-brand-neonBlue mt-1">
                                    <i class="ri-map-pin-line text-lg"></i>
                                </div>
                                <div>
                                    <h5 class="text-white font-medium mb-1">Area Layanan Utama</h5>
                                    <p class="text-slate-500 text-sm">Jakarta, Bogor, Depok, Tangerang, Bekasi dan wilayah sekitarnya.</p>
                                </div>
                            </div>
                            
                            <div class="flex items-start gap-4">
                                <div class="w-10 h-10 rounded-full bg-brand-neonBlue/10 flex items-center justify-center shrink-0 text-brand-neonBlue mt-1 ring-1 ring-brand-neonBlue/30">
                                    <i class="ri-whatsapp-line text-lg"></i>
                                </div>
                                <div>
                                    <h5 class="text-white font-medium mb-1">Fast Response WhatsApp</h5>
                                    <a href="https://wa.me/62821" target="_blank" class="text-brand-neonBlue hover:text-white transition-colors font-mono">+62 821-xxxx-xxxx</a>
                                </div>
                            </div>

                            <div class="flex items-start gap-4">
                                <div class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center shrink-0 text-brand-neonBlue mt-1">
                                    <i class="ri-mail-line text-lg"></i>
                                </div>
                                <div>
                                    <h5 class="text-white font-medium mb-1">Email Inquiry</h5>
                                    <a href="mailto:hello@angkasaadv.com" class="text-slate-400 hover:text-white transition-colors text-sm">hello@angkasaadv.com</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Action -->
                <div class="lg:w-7/12 p-10 md:p-16 border-t lg:border-t-0 lg:border-l border-white/5 flex items-center justify-center">
                    <div class="text-center w-full">
                        <div class="w-24 h-24 mx-auto bg-brand-neonBlue/10 rounded-full flex items-center justify-center mb-8 relative">
                            <div class="absolute inset-0 bg-brand-neonBlue/20 rounded-full animate-ping opacity-50"></div>
                            <i class="ri-whatsapp-fill text-5xl text-brand-neonBlue relative z-10"></i>
                        </div>
                        <h4 class="text-2xl font-bold text-white mb-3">Konsultasi Promo Harian 🔥</h4>
                        <p class="text-slate-400 text-sm mb-10 max-w-sm mx-auto">Kami akan membalas pesan Anda dalam hitungan menit untuk membahas proyek reklame impian Anda.</p>
                        
                        <a href="https://wa.me/62821" target="_blank" class="inline-flex items-center justify-center w-full sm:w-auto px-8 py-5 rounded-full bg-brand-neonBlue text-black font-bold text-lg hover:bg-white hover:shadow-[0_0_40px_rgba(0,240,255,0.7)] transition-all duration-300 gap-3 group relative overflow-hidden">
                            <i class="ri-chat-3-line text-xl group-hover:scale-110 transition-transform"></i>
                            <span class="relative z-10">Mulai Obrolan Sekarang</span>
                            <div class="absolute top-0 -inset-full h-full w-1/2 z-5 block transform -skew-x-12 bg-gradient-to-r from-transparent to-white opacity-40 group-hover:animate-[shine_1.5s_infinite]"></div>
                        </a>
                        <p class="text-xs text-slate-500 mt-6 flex justify-center items-center gap-1"><i class="ri-shield-check-line text-brand-neonBlue"></i> Kami menjamin kerahasiaan ide dan data Anda.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-brand-dark py-12 border-t border-white/5 relative z-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center gap-6">
            <div class="flex items-center gap-4">
                <a href="#" class="font-heading font-bold text-xl text-white group">
                    ANGKASA<span class="text-brand-neonBlue group-hover:text-white transition-colors duration-300">ADV</span>
                </a>
                <span class="hidden md:inline-block w-px h-5 bg-white/10"></span>
                <p class="text-slate-500 text-sm">© 2026 Hak Cipta Dilindungi.</p>
            </div>
            
            <div class="flex items-center gap-4">
                <a href="#" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center text-slate-400 hover:text-brand-neonBlue hover:bg-brand-neonBlue/10 transition-colors">
                    <i class="ri-instagram-line text-xl"></i>
                </a>
                <a href="#" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center text-slate-400 hover:text-brand-neonPink hover:bg-brand-neonPink/10 transition-colors">
                    <i class="ri-tiktok-fill text-xl"></i>
                </a>
                <a href="#" class="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center text-slate-400 hover:text-blue-500 hover:bg-blue-500/10 transition-colors">
                    <i class="ri-facebook-circle-fill text-xl"></i>
                </a>
            </div>
        </div>
    </footer>

    <!-- Image Modal for Portfolio -->
    <div id="image-modal" class="fixed inset-0 z-[100] bg-brand-dark/95 backdrop-blur-sm hidden items-center justify-center p-4 opacity-0 transition-opacity duration-300">
        <button id="close-modal" class="absolute top-6 right-6 w-12 h-12 rounded-full bg-white/5 border border-white/10 text-white flex items-center justify-center hover:bg-brand-neonPink hover:text-white hover:border-transparent transition-colors z-10 shadow-[0_4px_20px_rgba(0,0,0,0.5)]">
            <i class="ri-close-line text-2xl"></i>
        </button>
        <div class="max-w-5xl w-full flex items-center justify-center scale-95 transition-transform duration-300" id="modal-content">
            <img id="modal-img" src="" alt="Portfolio Image Preview" class="w-full max-h-[85vh] rounded-2xl shadow-[0_0_50px_rgba(0,0,0,1)] object-contain border border-white/10">
        </div>
    </div>

    <!-- Floating WA Button (Mobile primarily) -->
    <a href="#contact" class="fixed bottom-6 right-6 w-14 h-14 bg-[#25D366] text-white rounded-full flex items-center justify-center text-3xl shadow-[0_0_20px_rgba(37,211,102,0.5)] z-40 hover:scale-110 transition-transform md:hidden cursor-pointer" aria-label="Konsultasi WhatsApp">
        <i class="ri-whatsapp-line"></i>
    </a>

    <!-- Scripts -->
    <script src="script.js"></script>
</body>
</html>
"""

with open("index.html", "r", encoding="utf-8") as f:
    original = f.read()

# Make sure we don't duplicate
if "<!-- Portfolio Section -->" in original:
    print("Already built")
else:
    # find the comment "<!-- Portfolio section will be next... -->" and replace
    parts = original.split("<!-- Portfolio section will be next... -->")
    if len(parts) == 2:
        new_content = parts[0] + portfolio_html + contact_html
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Build success")
    else:
        # just replace the double </body> if it exists
        clean = original.replace("</body>\n</html>\n  </body>\n</html>", "")
        clean = clean.replace("</body>\n</html>", "")
        new_content = clean + portfolio_html + contact_html
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Build appended with cleaning")
