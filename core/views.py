from django.shortcuts import render

def main(request):
    return render(request, 'core/index.html')

def short_sleeves(request):
    product_data = [
        {"name": "Polo Shirts", "image": "short_sleeves_images/image1.png", "url": "https://pandabuy.allapp.link/co5bmbnm8ngrr7t9e570"},  
        {"name": "Bape Shirts","image": "short_sleeves_images/image2.jpg", "url": "https://pandabuy.allapp.link/co5bmt0gpf6pm1sj9ocg"},
        {"name": "Hellstar Shirts", "image": "short_sleeves_images/image3.webp", "url": "https://pandabuy.allapp.link/co5bn2fm8ngrr7t9e5lg"},
        {"name": "ESSENTIALS Shirts", "image": "short_sleeves_images/image4.avif", "url": "https://pandabuy.allapp.link/co5bnkprogtuqkqe2tj0"},
        {"name": "ASSC Shirts", "image": "short_sleeves_images/image5.avif", "url": "https://pandabuy.allapp.link/co5bntnm8ngrr7t9e67g"},
        

        {"name": "Vlone Shirts", "image": "short_sleeves_images/image6.jpg", "url": "https://pandabuy.allapp.link/co5bo5progtuqkqe2u00"},  
        {"name": "Sicko X Joy Shirts","image": "short_sleeves_images/image7.avif", "url": "https://pandabuy.allapp.link/co5bp78gpf6pm1sj9qe0"},
        {"name": "Blank Shirts", "image": "short_sleeves_images/image8.avif", "url": "https://pandabuy.allapp.link/co5bpb1rogtuqkqe2v2g"},
        {"name": "Yeezus Tour Merch Shirts", "image": "short_sleeves_images/image9.jpg", "url": "https://pandabuy.allapp.link/co5bphogpf6pm1sj9qo0"},
        {"name": "Jacquemes Artichoke Shirts", "image": "short_sleeves_images/image10.jpg", "url": "https://pandabuy.allapp.link/co5bpn1rogtuqkqe2vf0"},

        {"name": "Narcissict Merch", "image": "short_sleeves_images/image11.jpg", "url": "https://pandabuy.allapp.link/co5bqk9rogtuqkqe30e0"},   
        {"name": "Fat Tub Of Lard Shirts ","image": "short_sleeves_images/image12.avif", "url": "https://pandabuy.allapp.link/co5bqtvm8ngrr7t9e93g"},
        {"name": "Balenciaga Misplaced Shirt ", "image": "short_sleeves_images/image13.jpg", "url": "https://pandabuy.allapp.link/co5brb9rogtuqkqe3120"},
        {"name": "Vetements I did Nothing Shirt", "image": "short_sleeves_images/image14.avif", "url": "https://pandabuy.allapp.link/co5brqfm8ngrr7t9e9l0"},
        {"name": "30+ Travis Scot Merch ", "image": "short_sleeves_images/image15.avif", "url": "https://pandabuy.allapp.link/co5bs17m8ngrr7t9e9r0"},

        {"name": "OnlyFans Shirts", "image": "short_sleeves_images/image16.avif", "url": "https://pandabuy.allapp.link/co5bsevm8ngrr7t9ea80"}, 
        {"name": "Two piece Shirts ","image": "short_sleeves_images/image17.avif", "url": "https://pandabuy.allapp.link/co5bsl1rogtuqkqe31ug"},
        {"name": "Balenciaga Sporty B Shrunk Tee", "image": "short_sleeves_images/image18.jpg", "url": "https://pandabuy.allapp.link/co5bsr0gpf6pm1sj9t80"},
        {"name": "Balenciaga x Adidas Shirts", "image": "short_sleeves_images/image19.jpg", "url": "https://pandabuy.allapp.link/co5bvdprogtuqkqe34f0"},
        {"name": "Carti WLR Vampire Shirt White", "image": "short_sleeves_images/image20.avif", "url": "https://pandabuy.allapp.link/co5bvkvm8ngrr7t9ecug"},

        {"name": "Carti WLR Hell Merch ", "image": "short_sleeves_images/image21.avif", "url": "https://pandabuy.allapp.link/co5bvsogpf6pm1sj9vk0"},   
        {"name": "Corteiz Shirts ","image": "short_sleeves_images/image22.jpg", "url": "https://pandabuy.allapp.link/co5c068gpf6pm1sj9vu0"},
        {"name":"Carti x CPFM Merch White ", "image": "short_sleeves_images/image23.avif", "url": "https://pandabuy.allapp.link/co5c0l1rogtuqkqe35b0"},
        {"name": "Chrome Heart Cross Shirt", "image": "short_sleeves_images/image24.jpg", "url": "https://pandabuy.allapp.link/co5c0s1rogtuqkqe35l0"},
        {"name": "Dennis Rodman Tee ", "image": "short_sleeves_images/image25.avif", "url": "https://pandabuy.allapp.link/co5c0vvm8ngrr7t9ee30"},

        {"name": "Golf Wang Shirts ", "image": "short_sleeves_images/image26.avif", "url": "https://pandabuy.allapp.link/co5c2i7m8ngrr7t9ef60"},  
        {"name": "Frank Ocean Blonded Tee ","image": "short_sleeves_images/image27.jpg", "url": "https://pandabuy.allapp.link/co5c2oogpf6pm1sja250"},
        {"name":"Gallery Dept Alone in Silence Shirt ", "image": "short_sleeves_images/image28.jpg", "url": "https://pandabuy.allapp.link/co5c2uprogtuqkqe37d0"},
        {"name": "Fragment Clot Tee (2006)", "image": "short_sleeves_images/image29.jpg", "url": "https://weidian.info/jjxh6"},#dont work - wrong link
        {"name": "Fuck Me? Fuck You! Number Nine Shirt ", "image": "short_sleeves_images/image30.avif", "url": "https://pandabuy.allapp.link/co5f29ggpf6pm1sjcnk0"},

        {"name": "Gallery Dept Middle Finger Tee ", "image": "short_sleeves_images/image31.avif", "url": "https://pandabuy.allapp.link/co5f47fm8ngrr7t9hah0"},  
        {"name": "Gallery DEPT Hollywood T-shirt ","image": "short_sleeves_images/image32.jpg", "url": "https://pandabuy.allapp.link/co5f4e8gpf6pm1sjcpm0"},
        {"name":"Gothic Slogan Number Nine Shirt ", "image": "short_sleeves_images/image33.avif", "url": "https://pandabuy.allapp.link/co5f59nm8ngrr7t9hbjg"},#dont work - wrong link
        {"name": "Corteiz Grass T-shirts", "image": "short_sleeves_images/image34.jpg", "url": "https://pandabuy.allapp.link/co5f5jnm8ngrr7t9hbt0"},
        {"name": "FG T-shirts ", "image": "short_sleeves_images/image35.jpg", "url": "https://pandabuy.allapp.link/co5f5qnm8ngrr7t9hc60"},
        
        {"name": "Hellstar Grateful Dead Tee ", "image": "short_sleeves_images/image36.jpg", "url": "https://pandabuy.allapp.link/co5fha0gpf6pm1sjd5gg"},  
        {"name": "CPFM Hawaiian Shirt ","image": "short_sleeves_images/image37.avif", "url": "https://pandabuy.allapp.link/co5fhfvm8ngrr7t9hms0"},
        {"name":"Kapital Ringer Tee ", "image": "short_sleeves_images/image38.avif", "url": "https://pandabuy.allapp.link/co5fhonm8ngrr7t9hn60"},
        {"name": "House of Errors T-Shirt", "image": "short_sleeves_images/image39.avif", "url": "https://pandabuy.allapp.link/co5fi08gpf6pm1sjd640"},
        {"name": "Grateful Dead Shirt", "image": "short_sleeves_images/image40.jpg", "url": "https://pandabuy.allapp.link/co5fibprogtuqkqe6b9g"},

        {"name": "Dior Oblique Print Polo Shirts", "image": "short_sleeves_images/image41.jpg", "url": "https://pandabuy.allapp.link/co5fikhrogtuqkqe6bg0"},   
        {"name": "Joy Sicko Tee ","image": "short_sleeves_images/image42.avif", "url": "https://pandabuy.allapp.link/co5fjp0gpf6pm1sjd7m0"},
        {"name":"Playboi Carti Falling in Reverse WLR Shirt", "image": "short_sleeves_images/image43.avif", "url": "https://pandabuy.allapp.link/co5fju7m8ngrr7t9hp80"},
        {"name": "Led Zeppelin Number Nine Shirt ", "image": "short_sleeves_images/image44.avif", "url": "https://pandabuy.allapp.link/co5fkn9rogtuqkqe6d5g"},
        {"name": "Playboi Carti WLR Merch", "image": "short_sleeves_images/image45.avif", "url": "https://pandabuy.allapp.link/co5fkvhrogtuqkqe6de0"},

        {"name": "10+ Vintage Rapper Graphic Tees", "image": "short_sleeves_images/image46.avif", "url": "https://pandabuy.allapp.link/co5fd57m8ngrr7t9hj6g"},   
        {"name": "Trapstar Jerseys ","image": "short_sleeves_images/image47.jpg", "url": "https://pandabuy.allapp.link/co5ffiprogtuqkqe693g"},
        {"name":"Number Nine 3 Mickey Shirts", "image": "short_sleeves_images/image48.avif", "url": "https://pandabuy.allapp.link/co5fg0ggpf6pm1sjd4jg"},
        {"name": "Prada Dress Shirts", "image": "short_sleeves_images/image49.avif", "url": "https://pandabuy.allapp.link/co5fg8hrogtuqkqe69ig"},
        {"name": "Rick Owens DRKR Tee", "image": "short_sleeves_images/image50.jpg", "url": "https://pandabuy.allapp.link/co5fguprogtuqkqe6a5g"},

        {"name": "Kurt Cobain Number Nine ", "image": "short_sleeves_images/image51.avif", "url": "https://pandabuy.allapp.link/co5fbkggpf6pm1sjd07g"},  
        {"name": "Nirvana Shirt","image": "short_sleeves_images/image52.avif", "url": "https://pandabuy.allapp.link/co5fbsfm8ngrr7t9hhlg"},
        {"name":"Loved Gun Number Nine T Shirt", "image": "short_sleeves_images/image53.avif", "url": "https://pandabuy.allapp.link/co5fceprogtuqkqe65vg"},
        {"name": "Ken Car$on Teen X Merch ", "image": "short_sleeves_images/image54.avif", "url": "https://pandabuy.allapp.link/co5fcm0gpf6pm1sjd19g"},
        {"name": "Narcissist Merch", "image": "short_sleeves_images/image55.avif", "url": "https://pandabuy.allapp.link/co5fct9rogtuqkqe66d0"},

        {"name": "Nirvana Vintage Shirts", "image": "short_sleeves_images/image56.jpg", "url": "https://pandabuy.allapp.link/co5f8lfm8ngrr7t9het0"},  
        {"name": "Undercover x CDG Shirt","image": "short_sleeves_images/image57.avif", "url": "https://pandabuy.allapp.link/co5f8shrogtuqkqe62n0"},
        {"name":"Undercover Scab Scorpion T-Shirt", "image": "short_sleeves_images/image58.avif", "url": "https://pandabuy.allapp.link/co5f95fm8ngrr7t9hf9g"},
        {"name": "Mood Swings T-Shirts", "image": "short_sleeves_images/image59.avif", "url": "https://pandabuy.allapp.link/co5f9fogpf6pm1sjcuf0"},
        {"name": "Rick Owens Fog Machine T Shirts", "image": "short_sleeves_images/image60.jpg", "url": "https://pandabuy.allapp.link/co5favhrogtuqkqe64ig"},

        {"name": "Playboi Carti Anime Shirt White ", "image": "short_sleeves_images/image61.avif", "url": "https://pandabuy.allapp.link/co5f7efm8ngrr7t9hdmg"}, 
        {"name": "Eyeball Vintage Tee ","image": "short_sleeves_images/image62.jpg", "url": "https://pandabuy.allapp.link/co5f7l1rogtuqkqe61gg"},
        {"name":"Kapital Two Tone Shirts", "image": "short_sleeves_images/image63.avif", "url": "https://pandabuy.allapp.link/co5f7sfm8ngrr7t9he50"},
        {"name": "Carti WLR Hell Merch White ", "image": "short_sleeves_images/image64.avif", "url": "https://pandabuy.allapp.link/co5f850gpf6pm1sjct7g"},
        {"name": "Saint Michael Virgin Mary Tee", "image": "short_sleeves_images/image65.avif", "url": "https://pandabuy.allapp.link/co5f8bhrogtuqkqe6270"},

        
    ]
    return render(request, 'core/short_sleeves.html', {'product_data': product_data})

def long_sleeves(request):
    product_data = [
        {"name": "Curly Stussy Sweatshirt", "image": "long_sleeves_images/image1.jpg", "url": "https://pandabuy.allapp.link/co50lj0gpf6oar2jdnlg"},
        {"name": "Small Logo Nike Sweatshirt", "image": "long_sleeves_images/image2.jpg", "url": "https://pandabuy.allapp.link/co50lp0gpf6oar2jdno0"},
        {"name": "Chrome Heart Sweatshirt", "image": "long_sleeves_images/image3.jpg", "url": "https://pandabuy.allapp.link/co50luhrogtreqrk5l2g"},
        {"name": "Moncler Sweatshirt", "image": "long_sleeves_images/image4.jpg", "url": "https://pandabuy.allapp.link/co50m4ogpf6oar2jdo0g"},
        {"name": "Carhartt Half Zip", "image": "long_sleeves_images/image5.jpg", "url": "https://pandabuy.allapp.link/co50mb8gpf6oar2jdo2g"},

        {"name": "Orange Autumn Chrome Heart Sweatshirt", "image": "long_sleeves_images/image6.jpg", "url": "https://pandabuy.allapp.link/co50n1hrogtreqrk5lfg"},
        {"name": "Bape Sweatshirt", "image": "long_sleeves_images/image7.avif", "url": "https://pandabuy.allapp.link/co50rehrogtreqrk5n30"},
        {"name": "Hockey X Balenciaga Jersey Sweatshirt", "image": "long_sleeves_images/image8.jpg", "url": "https://pandabuy.allapp.link/co50rkprogtreqrk5n40"},
        {"name": "Balenciaga Campaign Sweatshirt", "image": "long_sleeves_images/image9.jpg", "url": "https://pandabuy.allapp.link/co50tl90b4mjcscn8cfg"},
        {"name": "Balenciaga Pride Crewneck", "image": "long_sleeves_images/image10.jpg", "url": "https://pandabuy.allapp.link/co50tq90b4mjcscn8cj0"},

        {"name": "Destroyed Chrome Heart Sweatshirt", "image": "long_sleeves_images/image11.jpg", "url": "https://pandabuy.allapp.link/co516gh0b4mjcscn8gbg"},
        {"name": "ERD Knit Sweatshirt", "image": "long_sleeves_images/image12.jpg", "url": "https://pandabuy.allapp.link/co516bprogtreqrk5r90"},
        {"name": "ERD Lou Reed Sweatshirt", "image": "long_sleeves_images/image13.avif", "url": "https://pandabuy.allapp.link/co51628gpf6oar2jdtp0"},
        {"name": "Frank Ocean Sweatshirt", "image": "long_sleeves_images/image14.avif", "url": "https://pandabuy.allapp.link/co515logpf6oar2jdtk0"},
        {"name": "Gallery Dept Hollywood Sweatshirt", "image": "long_sleeves_images/image15.jpg", "url": "https://pandabuy.allapp.link/co515fhrogtreqrk5r1g"},

        {"name": "Golf Crewnecks", "image": "long_sleeves_images/image16.avif", "url": "https://pandabuy.allapp.link/co512n8gpf6oar2jdskg"},
        {"name": "Gallery Dept Washed Sweatshirt", "image": "long_sleeves_images/image17.avif", "url": "https://pandabuy.allapp.link/co512j90b4mjcscn8f0g"},
        {"name": "Brad Pitt Sweatshirt", "image": "long_sleeves_images/image18.jpg", "url": "https://pandabuy.allapp.link/co512c1rogtreqrk5q6g"},
        {"name": "Kapital Bone Sweatshirt", "image": "long_sleeves_images/image19.avif", "url": "https://pandabuy.allapp.link/co512590b4mjcscn8epg"},
        {"name": "LV Numbers Jacquard Sweatshirt", "image": "long_sleeves_images/image20.avif", "url": "https://pandabuy.allapp.link/co511s0gpf6oar2jdscg"},

        {"name": "Mastermind Crewneck", "image": "long_sleeves_images/image21.jpg", "url": "https://pandabuy.allapp.link/co510c10b4mjcscn8dsg"},
        {"name": "Cactus Plant X Nike Sweatshirt", "image": "long_sleeves_images/image22.jpg", "url": "https://pandabuy.allapp.link/co5108ggpf6oar2jdrp0"},
        {"name": "Nike Sweatshirt", "image": "long_sleeves_images/image23.jpg", "url": "https://pandabuy.allapp.link/co5101hrogtreqrk5p5g"},
        {"name": "Maison Margiela Knit Sweatshirt", "image": "long_sleeves_images/image24.jpg", "url": "https://pandabuy.allapp.link/co50vt90b4mjcscn8dng"},
        {"name": "Stussy X Nike Sweatshirt", "image": "long_sleeves_images/image25.jpg", "url": "https://pandabuy.allapp.link/co50voprogtreqrk5ovg"},

        {"name": "Knitted Female Graffiti Crewneck", "image": "long_sleeves_images/image26.avif", "url": "https://pandabuy.allapp.link/co50v9p0b4mjcscn8dag"},
        {"name": "RafSimons Knitted Sweatshirt", "image": "long_sleeves_images/image27.avif", "url": "https://pandabuy.allapp.link/co50v10gpf6oar2jdr7g"},
        {"name": "Pool X Stussy Knitted Sweatshirt", "image": "long_sleeves_images/image28.avif", "url": "https://pandabuy.allapp.link/co50upp0b4mjcscn8d3g"},
        {"name": "SickSidSweatshirt", "image": "long_sleeves_images/image29.avif", "url": "https://pandabuy.allapp.link/co50ua10b4mjcscn8co0"},
        {"name": "Undercover x Evangelion Crewneck", "image": "long_sleeves_images/image30.avif", "url": "https://pandabuy.allapp.link/co50u1ogpf6oar2jdqrg"},
    ]
    return render(request, 'core/long_sleeves.html', {'product_data': product_data})

def pants(request):
    product_data = [
        {"name": "SPIDER Sweatpants", "image": "pants_images/image1.jpg", "url": "https://pandabuy.allapp.link/co5am39rogtuqkqe1vh0"},
        {"name": "Nike Sweatpants", "image": "pants_images/image2.jpg", "url": "https://pandabuy.allapp.link/co5amavm8ngrr7t9d8jg"},
        {"name": "Demin Tear Sweatpants", "image": "pants_images/image3.webp", "url": "https://pandabuy.allapp.link/co5amgggpf6pm1sj8rk0"},
        {"name": "Demin Tear Jeans", "image": "pants_images/image4.jpg", "url": "https://pandabuy.allapp.link/co5amp1rogtuqkqe204g"},
        {"name": "Carhartt Casual Pants", "image": "pants_images/image5.avif", "url": "https://pandabuy.allapp.link/co5an0hrogtuqkqe20c0"},


        {"name": "Minus Two Cargos", "image": "pants_images/image6.webp", "url": "https://pandabuy.allapp.link/co5an6nm8ngrr7t9d9cg"},
        {"name": "Jacov Pants", "image": "pants_images/image7.jpg", "url": "https://pandabuy.allapp.link/co5anc0gpf6pm1sj8sa0"},
        {"name": "Vintage Bape Jeans", "image": "pants_images/image8.avif", "url": "https://pandabuy.allapp.link/co5anj8gpf6pm1sj8sig"},
        {"name": "Revenge Jeans", "image": "pants_images/image9.avif", "url": "https://pandabuy.allapp.link/co5anr7m8ngrr7t9da1g"},
        {"name": "Supreme X Burberry Denim Pants", "image": "pants_images/image10.jpg", "url": "hhttps://pandabuy.allapp.link/co5ap4fm8ngrr7t9db90"},


        {"name": "Supreme X Yankee Denim Pants", "image": "pants_images/image11.jpg", "url": "https://pandabuy.allapp.link/co5apc0gpf6pm1sj8tlg"},
        {"name": "Ripped Flared Jeans", "image": "pants_images/image12.avif", "url": "https://pandabuy.allapp.link/co5app7m8ngrr7t9dbl0"},
        {"name": "Endless Jeans", "image": "pants_images/image13.jpg", "url": "https://pandabuy.allapp.link/co5aq29rogtuqkqe22rg"},
        {"name": "Balenciaga Flared Jeans", "image": "pants_images/image14.avif", "url": "https://pandabuy.allapp.link/co5aqa7m8ngrr7t9dc00"},
        {"name": "Palm Angel Pants", "image": "pants_images/image15.avif", "url": "https://pandabuy.allapp.link/co5aqhfm8ngrr7t9dc80"},

        {"name": "Gallery Dept Pants", "image": "pants_images/image16.jpg", "url": "https://pandabuy.allapp.link/co5au4ogpf6pm1sj913g"},
        {"name": "CPFM Pants", "image": "pants_images/image17.jpg", "url": "https://pandabuy.allapp.link/co5auaggpf6pm1sj91a0"},
        {"name": "Nike Tech FLeece Pants", "image": "pants_images/image18.webp", "url": "https://pandabuy.allapp.link/co5aug8gpf6pm1sj91hg"},
        {"name": "Camo Pants", "image": "pants_images/image19.avif", "url": "https://pandabuy.allapp.link/co5ava7m8ngrr7t9dg2g"},
        {"name": "Purple Jeans", "image": "pants_images/image20.jpg", "url": "https://pandabuy.allapp.link/co5avl7m8ngrr7t9dge0"},




    ]
    return render(request, 'core/pants.html', {'product_data': product_data})

def shorts(request):
    product_data = [
        {"name": "EE Shorts", "image": "shorts_images/image1.jpg", "url": "https://pandabuy.allapp.link/co5fo7ogpf6pm1sjdcbg"},
        {"name": "ASRV Shorts", "image": "shorts_images/image2.avif", "url": "https://pandabuy.allapp.link/co5fohvm8ngrr7t9httg"},
        {"name": "KINETIC Shorts", "image": "shorts_images/image3.jpg", "url": "https://pandabuy.allapp.link/co5fopnm8ngrr7t9hu4g"},
        {"name": "NORTH FACE Shorts", "image": "shorts_images/image4.jpg", "url": "https://weidian.com/item.html?itemID=4397132802"},#dont work - ded linnk
        {"name": "RHUDE Shorts", "image": "shorts_images/image5.png", "url": "https://pandabuy.allapp.link/co5fphfm8ngrr7t9huv0"},

        {"name": "Jordan Shorts", "image": "shorts_images/image6.jpg", "url": "https://pandabuy.allapp.link/co5fq47m8ngrr7t9hveg"},
        {"name": "Nike NBA Shorts", "image": "shorts_images/image7.jpg", "url": "https://weidian.info/vp9sc"},#dont work - ded link
        {"name": "Billionaire Boys Club Shorts", "image": "shorts_images/image8.png", "url": "https://pandabuy.allapp.link/co5fsp0gpf6pm1sjdh00"},
        {"name": "Represent Shorts", "image": "shorts_images/image9.avif", "url": "https://pandabuy.allapp.link/co5ft1progtuqkqe6mig"},
        {"name": "Chrome Heart Shorts", "image": "shorts_images/image10.png", "url": "https://pandabuy.allapp.link/co5ftg1rogtuqkqe6n0g"},

        {"name": "Bape Shorts", "image": "shorts_images/image11.jpg", "url": "https://pandabuy.allapp.link/co5fvo1rogtuqkqe6pf0"},
        {"name": "Revenge Shorts", "image": "shorts_images/image12.avif", "url": "https://pandabuy.allapp.link/co5g011rogtuqkqe6png"},
        {"name": "FOG ESSENTIALS Shorts", "image": "shorts_images/image13.avif", "url": "https://pandabuy.allapp.link/co5g0b1rogtuqkqe6q80"},
        {"name": "Travis Scot Cactus Jack Shorts", "image": "shorts_images/image14.jpg", "url": "https://pandabuy.allapp.link/co5g9gprogtuqkqe73m0"},
        {"name": "Corteiz Shorts", "image": "shorts_images/image15.jpg", "url": "https://pandabuy.allapp.link/co5g8e7m8ngrr7t9ie8g"},


        {"name": "Fendi Shorts", "image": "shorts_images/image16.webp", "url": "https://pandabuy.allapp.link/co5fttogpf6pm1sjdi70"},
        {"name": "Raptors Shorts", "image": "shorts_images/image17.png", "url": "https://pandabuy.allapp.link/co5fu50gpf6pm1sjdigg"},
        {"name": "Stussy Shorts", "image": "shorts_images/image18.png", "url": "https://pandabuy.allapp.link/co5fuc0gpf6pm1sjding"},
        {"name": "Minus Two Cargo Shorts", "image": "shorts_images/image19.jpg", "url": "https://pandabuy.allapp.link/co5fv6vm8ngrr7t9i44g"},
        {"name": "Trapstar Shorts", "image": "shorts_images/image20.png", "url": "https://pandabuy.allapp.link/co5fvgggpf6pm1sjdk2g"},

    ]
    return render(request, 'core/shorts.html', {'product_data': product_data})

def shoes(request):
    product_data = [
        {"name": "Travis Scot 1 Low", "image": "shoes_images/image1.jpg", "url": "https://pandabuy.allapp.link/co5b0pnm8ngrr7t9dhf0"},
        {"name": "LV Slides", "image": "shoes_images/image2.jpg", "url": "https://pandabuy.allapp.link/co5b12nm8ngrr7t9dhmg"},
        {"name": "LV Trainers", "image": "shoes_images/image3.jpg", "url": "https://pandabuy.allapp.link/co5b22nm8ngrr7t9dij0"},
        {"name": "NB 550", "image": "shoes_images/image4.jpg", "url": "https://pandabuy.allapp.link/co5b2anm8ngrr7t9diog"},
        {"name": "Kobe 4 / 5 / 6 / 8", "image": "shoes_images/image5.webp", "url": "https://pandabuy.allapp.link/co5b3qprogtuqkqe2atg"},

        {"name": "SB Lobster Dunk Lows", "image": "shoes_images/image6.jpg", "url": "https://pandabuy.allapp.link/co5bahprogtuqkqe2gmg"},
        {"name": "SB Dunk Lows", "image": "shoes_images/image7.jpg", "url": "https://pandabuy.allapp.link/co5banhrogtuqkqe2gtg"},
        {"name": "LV X SB Dunk Lows", "image": "shoes_images/image8.png", "url": "https://pandabuy.allapp.link/co5bauggpf6pm1sj9c0g"},
        {"name": "EBAY X SB Dunk Lows", "image": "shoes_images/image9.jpg", "url": "https://pandabuy.allapp.link/co5bb99rogtuqkqe2heg"},
        {"name": "PARIS X SB DUNK Lows", "image": "shoes_images/image10.jpg", "url": "https://pandabuy.allapp.link/co5bbffm8ngrr7t9dqeg"},

        {"name": "Rare AJ1", "image": "shoes_images/image11.jpg", "url": "https://pandabuy.allapp.link/co5b8f0gpf6pm1sj99ug"},
        {"name": "AJ1 Stage Haze", "image": "shoes_images/image12.jpg", "url": "https://pandabuy.allapp.link/co5b8k8gpf6pm1sj9a20"},
        {"name": "30+ AJ1 Colorways", "image": "shoes_images/image13.jpg", "url": "https://pandabuy.allapp.link/co5b8p8gpf6pm1sj9a50"},
        {"name": "Off White AJ1 Blue High ", "image": "shoes_images/image14.jpg", "url": "https://pandabuy.allapp.link/co5b900gpf6pm1sj9ac0"},
        {"name": "Off White AJ1 Chicago High ", "image": "shoes_images/image15.jpg", "url": "https://pandabuy.allapp.link/co5b99ggpf6pm1sj9ajg"},

        {"name": "20+ AJ4", "image": "shoes_images/image16.webp", "url": "https://pandabuy.allapp.link/co5b651rogtuqkqe2cpg"},
        {"name": "Levi X AJ4", "image": "shoes_images/image17.jpg", "url": "https://pandabuy.allapp.link/co5b6anm8ngrr7t9dltg"},#dont work - stopped selliing
        {"name": "More AJ4", "image": "shoes_images/image18.jpg", "url": "https://pandabuy.allapp.link/co5b7a7m8ngrr7t9dmqg"},
        {"name": "AJ1 Low Nothing But New  ", "image": "shoes_images/image19.jpg", "url": "https://pandabuy.allapp.link/co5b7fggpf6pm1sj98u0"},
        {"name": "AJ1 Low Lakers Blue Yellow", "image": "shoes_images/image20.jpg", "url": "https://pandabuy.allapp.link/co5b858gpf6pm1sj99j0"},
    ]
    return render(request, 'core/shoes.html', {'product_data': product_data})

def accessories(request):
    product_data = [
        {"name": "Carti Phonecase", "image": "accessories_images/image1.webp", "url": "https://pandabuy.allapp.link/co4ssfprogtreqrk2vq0"},
        {"name": "Chrome Heart Bracelet", "image": "accessories_images/image2.avif", "url": "https://pandabuy.allapp.link/co4stap0b4mjcscn5ki0"},
        {"name": "Chrome Heart Necklace", "image": "accessories_images/image3.jpg", "url": "https://pandabuy.allapp.link/co4svs8gpf6oar2jb5vg"},
        {"name": "Carhartt Hats", "image": "accessories_images/image4.jpg", "url": "https://pandabuy.allapp.link/co4t04ogpf6oar2jb640"},
        {"name": "Nike Socks", "image": "accessories_images/image5.jpg", "url": "https://pandabuy.allapp.link/co4t0e8gpf6oar2jb6e0"},

        {"name": "Chrome Heart Hats", "image": "accessories_images/image6.avif", "url": "https://pandabuy.allapp.link/co4t0n90b4mjcscn5nm0"},
        {"name": "Corteiz Hats", "image": "accessories_images/image7.avif", "url": "https://pandabuy.allapp.link/co4t1u10b4mjcscn5op0"},
        {"name": "Gallery Dept Hats", "image": "accessories_images/image8.jpg", "url": "https://pandabuy.allapp.link/co4t299rogtreqrk34ug"},
        {"name": "Moncler Beanies", "image": "accessories_images/image9.jpg", "url": "https://pandabuy.allapp.link/co4t2i0gpf6oar2jb8cg"},
        {"name": "Stone Island Beanies", "image": "accessories_images/image10.jpg", "url": "https://pandabuy.allapp.link/co4t2s90b4mjcscn5psg"},


        {"name": "Minus Two Beanies", "image": "accessories_images/image11.jpg", "url": "https://pandabuy.allapp.link/co4t6aogpf6oar2jbbv0"},
        {"name": "Curly Stussy Beanie", "image": "accessories_images/image12.png", "url": "https://pandabuy.allapp.link/co4t6lhrogtreqrk397g"},
        {"name": "Star Beanie", "image": "accessories_images/image13.avif", "url": "https://pandabuy.allapp.link/co4t6tggpf6oar2jbcog"},
        {"name": "Bear Beanie", "image": "accessories_images/image14.png", "url": "https://pandabuy.allapp.link/co4t7a1rogtreqrk39q0"},
        {"name": "Graphic Beanies", "image": "accessories_images/image15.avif", "url": "https://pandabuy.allapp.link/co4t7l9rogtreqrk3a3g"},

        {"name": "Chrome Heart Beanies", "image": "accessories_images/image16.avif", "url": "https://pandabuy.allapp.link/co4t8o0gpf6oar2jbe90"},
        {"name": "Prada Hats", "image": "accessories_images/image17.jpg", "url": "https://pandabuy.allapp.link/co4t909rogtreqrk3bfg"},
        {"name": "Bape Beanies", "image": "accessories_images/image18.jpg", "url": "https://pandabuy.allapp.link/co4t9bh0b4mjcscn5v7g"},
        {"name": "Lv Scarf +  Beanies", "image": "accessories_images/image19.jpg", "url": "https://weidian.info/ecpzf"},#dont work
        {"name": "Durags", "image": "accessories_images/image20.jpg", "url": "https://pandabuy.allapp.link/co4ta7ogpf6oar2jbfk0"},

        {"name": "20+ Chrome Hearts Bracelets", "image": "accessories_images/image21.jpg", "url": "https://pandabuy.allapp.link/co4ukr8gpf6oar2jcil0"},
        {"name": "Chrome Hearts Rolex Watch", "image": "accessories_images/image22.avif", "url": "https://pandabuy.allapp.link/co4ul7hrogtreqrk4h10"},
        {"name": "GOLF Ring", "image": "accessories_images/image23.avif", "url": "https://pandabuy.allapp.link/co4ulghrogtreqrk4h9g"},
        {"name": "Sliver Homes Bracelet", "image": "accessories_images/image24.avif", "url": "https://pandabuy.allapp.link/co4uloggpf6oar2jcj6g"},
        {"name": "Chrome Hearts Cross Bracelet", "image": "accessories_images/image25.jpg", "url": "https://pandabuy.allapp.link/co4ulv10b4mjcscn75v0"},

        {"name": "Alabaster Inspired Rings", "image": "accessories_images/image26.avif", "url": "https://pandabuy.allapp.link/co4umb9rogtreqrk4hr0"},
        {"name": "Alyx Transparent Bracelet + Necklace", "image": "accessories_images/image27.avif", "url": "https://pandabuy.allapp.link/co4umj9rogtreqrk4hvg"},
        {"name": "Black Skull Vivienne Chain", "image": "accessories_images/image28.jpg", "url": "https://pandabuy.allapp.link/co4un11rogtreqrk4i80"},
        {"name": "Bat Necklace", "image": "accessories_images/image29.jpg", "url": "https://pandabuy.allapp.link/co4unb0gpf6oar2jcka0"},
        {"name": "CCP Teeth Necklace", "image": "accessories_images/image30.avif", "url": "https://pandabuy.allapp.link/co4unh1rogtreqrk4ihg"},

        {"name": "Chrome Heart Watch band", "image": "accessories_images/image31.avif", "url": "https://pandabuy.allapp.link/co4uqq10b4mjcscn79jg"},
        {"name": "20+ Chrome Heart Rings", "image": "accessories_images/image32.avif", "url": "https://pandabuy.allapp.link/co4uqjp0b4mjcscn79d0"},
        {"name": "Chrome Hearts Silicone Necklaces", "image": "accessories_images/image33.avif", "url": "https://pandabuy.allapp.link/co4ur090b4mjcscn79p0"},
        {"name": "Chrome Hearts Floral Bracelet", "image": "accessories_images/image34.jpg", "url": "https://pandabuy.allapp.link/co4ur710b4mjcscn79vg"},
        {"name": "Chrome Hearts Crown Cross Ring", "image": "accessories_images/image35.jpg", "url": "https://pandabuy.allapp.link/co4urd10b4mjcscn7a50"},

        {"name": "Chrome Hearts Cuban Bracelet", "image": "accessories_images/image36.jpg", "url": "https://pandabuy.allapp.link/co4usp90b4mjcscn7bd0"},
        {"name": "Chrome Hearts Flower Earrings", "image": "accessories_images/image37.jpg", "url": "https://pandabuy.allapp.link/co4ut0h0b4mjcscn7bhg"},
        {"name": "Chrome Hearts Dagger Dangling Earrings", "image": "accessories_images/image38.jpg", "url": "https://pandabuy.allapp.link/co4vapprogtreqrk4vkg"},
        {"name": "Chrome Hearts flower leather bracelet", "image": "accessories_images/image39.jpg", "url": "https://pandabuy.allapp.link/co4vavp0b4mjcscn7k40"},
        {"name": "Chrome Hearts Forever Ring", "image": "accessories_images/image40.jpg", "url": "https://pandabuy.allapp.link/co4vb790b4mjcscn7kbg"},

        {"name": "Frank Ocean Homer Necklaces ", "image": "accessories_images/image41.avif", "url": "https://pandabuy.allapp.link/co4vco1rogtreqrk50ig"},
        {"name": "Golf Wang Flower Necklace", "image": "accessories_images/image42.avif", "url": "https://pandabuy.allapp.link/co4vcsprogtreqrk50l0"},
        {"name": " Homer Necklace", "image": "accessories_images/image43.avif", "url": "https://pandabuy.allapp.link/co4vd1ogpf6oar2jd2og"},
        {"name": "LV Monogram Party Necklace", "image": "accessories_images/image44.jpg", "url": "https://pandabuy.allapp.link/co4vd6p0b4mjcscn7lcg"},
        {"name": "Green Chrome Hearts Bead Bracelet", "image": "accessories_images/image45.jpg", "url": "https://pandabuy.allapp.link/co4vdc90b4mjcscn7lhg"},
  
    ]
    return render(request, 'core/accessories.html', {'product_data': product_data})


def sweaters(request):
    product_data = [
        {"name": "SPIDER Hoodie", "image": "sweaters_images/image1.webp", "url": "https://pandabuy.allapp.link/co8pvjnm8ngrr7tbit5g"},
        {"name": "FOG Essentials Hoodie", "image": "sweaters_images/image2.webp", "url": "https://pandabuy.allapp.link/co8pvuggpf6pm1sle27g"},
        {"name": "4TUNE Full Zipup", "image": "sweaters_images/image3.jpg", "url": "https://pandabuy.allapp.link/co8q729rogtuqkqg78jg"},
        {"name": "Travis Scot Cactus Jack Zipup", "image": "sweaters_images/image4.jpg", "url": "https://pandabuy.allapp.link/co8q1kogpf6pm1sle3dg"},
        {"name": "Polo Ralph Lauren Zipup", "image": "sweaters_images/image5.jpg", "url": "https://pandabuy.allapp.link/co8q6r7m8ngrr7tbj1ug"},

        {"name": "Chrome Heart Zipper/Hoodie", "image": "sweaters_images/image6.avif", "url": "https://pandabuy.allapp.link/co8rb0hrogtuqkqg8290"},
        {"name": "Saint Michael Graffiti Hoodie", "image": "sweaters_images/image7.avif", "url": "https://pandabuy.allapp.link/co8rc3ggpf6pm1slf1g0"},
        {"name": "Playboi Carti Hoodie", "image": "sweaters_images/image8.avif", "url": "https://pandabuy.allapp.link/co8rcuogpf6pm1slf270"},
        {"name": "Ye Must be Born Again Hoodie", "image": "sweaters_images/image9.jpg", "url": "https://pandabuy.allapp.link/co8rdanm8ngrr7tbjtrg"},
        {"name": "123 FOG Hoodie", "image": "sweaters_images/image10.jpg", "url": "https://pandabuy.allapp.link/co8rdg1rogtuqkqg83q0"},

        {"name": "Cuwu Amikaki Graphic printed hoodie", "image": "sweaters_images/image11.avif", "url": "https://pandabuy.allapp.link/co8rg3hrogtuqkqg85jg"},
        {"name": "Palm Angels Web Hoodie", "image": "sweaters_images/image12.avif", "url": "https://pandabuy.allapp.link/co8rg87m8ngrr7tbjvq0"},
        {"name": "Yeezy Gap Hoodie", "image": "sweaters_images/image13.avif", "url": "https://pandabuy.allapp.link/co8rgd9rogtuqkqg85pg"},
        {"name": "Travis Scot MCD Hoodie", "image": "sweaters_images/image14.jpg", "url": "https://pandabuy.allapp.link/co8rghogpf6pm1slf4ug"},
        {"name": "Stussy 8Ball Hoodie", "image": "sweaters_images/image15.avif", "url": "https://pandabuy.allapp.link/co8rgpnm8ngrr7tbk0b0"},

        {"name": "Trapstar X Dave hoodie", "image": "sweaters_images/image16.avif", "url": "https://pandabuy.allapp.link/co8rh2ggpf6pm1slf56g"},
        {"name": "Vetements Hoodie", "image": "sweaters_images/image17.webp", "url": "https://pandabuy.allapp.link/co8rh6ggpf6pm1slf590"},
        {"name": "Off White Hoodie", "image": "sweaters_images/image18.jpg", "url": "https://pandabuy.allapp.link/co8rhbprogtuqkqg86k0"},
        {"name": "Y2K Titanic Hoodie", "image": "sweaters_images/image19.png", "url": "https://pandabuy.allapp.link/co8rhi8gpf6pm1slf5k0"},
        {"name": "Vintage Sicko Hoodie", "image": "sweaters_images/image20.avif", "url": "https://pandabuy.allapp.link/co8rho9rogtuqkqg86t0"},

        {"name": "Saint hoodie", "image": "sweaters_images/image21.avif", "url": "https://pandabuy.allapp.link/co8rht9rogtuqkqg86vg"},
        {"name": "Mini Nike Swoosh Hoodie", "image": "sweaters_images/image22.jpg", "url": "https://pandabuy.allapp.link/co8ri4vm8ngrr7tbk1ag"},
        {"name": "Bape Full Head Zipup", "image": "sweaters_images/image23.jpg", "url": "https://pandabuy.allapp.link/co8rig8gpf6pm1slf69g"},
        {"name": "Batman Bape Full Head Zipup", "image": "sweaters_images/image24.avif", "url": "https://pandabuy.allapp.link/co8rilnm8ngrr7tbk1og"},
        {"name": "Star Bape Full Head Zipup", "image": "sweaters_images/image25.avif", "url": "https://pandabuy.allapp.link/co8ripvm8ngrr7tbk1sg"},

        {"name": "Travis Scot X Kaws Zipup", "image": "sweaters_images/image26.avif", "url": "https://pandabuy.allapp.link/co8rk30gpf6pm1slf7j0"},
        {"name": "Rick Owns Full Zip", "image": "sweaters_images/image27.avif", "url": "https://pandabuy.allapp.link/co8rk7hrogtuqkqg88ig"},
        {"name": "All Shadows Zipup", "image": "sweaters_images/image28.jpg", "url": "https://pandabuy.allapp.link/co8rkc8gpf6pm1slf7tg"},
        {"name": "Mastermind Travis Scot Zipup", "image": "sweaters_images/image29.avif", "url": "https://pandabuy.allapp.link/co8rkgggpf6pm1slf810"},
        {"name": "Burberry Zipup", "image": "sweaters_images/image30.jpg", "url": "https://pandabuy.allapp.link/co8rkk8gpf6pm1slf83g"},

        {"name": "Stussy Zipup", "image": "sweaters_images/image31.jpg", "url": "https://pandabuy.allapp.link/co8rkp1rogtuqkqg88tg"},
        {"name": "CP Zipup", "image": "sweaters_images/image32.jpg", "url": "https://pandabuy.allapp.link/co8rkvfm8ngrr7tbk3q0"},
        {"name": "High Zipup Blank", "image": "sweaters_images/image33.avif", "url": "https://pandabuy.allapp.link/co8rl4ggpf6pm1slf8jg"},
        {"name": "Wrld Krisis Full Head Zipup", "image": "sweaters_images/image34.jpg", "url": "https://pandabuy.allapp.link/co8rl8fm8ngrr7tbk400"},
        {"name": "Ver Blee Full Head Zipup", "image": "sweaters_images/image35.avif", "url": "https://pandabuy.allapp.link/co8rlchrogtuqkqg89b0"},
    ]
    return render(request, 'core/sweaters.html', {'product_data': product_data})

def jackets(request):
     product_data = [
        {"name": " Canada Goose Men/Women Winter Gilet Vest", "image": "jackets_images/image1.webp", "url": "https://pandabuy.allapp.link/co4vuap0b4mjcscn7u6g"},
        {"name": "THE NORTH FACE 1996 Retro Nuptse Puffer Jacket", "image": "jackets_images/image2.jpg", "url": "https://pandabuy.allapp.link/co4vujprogtreqrk5ajg"},
        {"name": "Nike X Tiffany Embroidered Jacket", "image": "jackets_images/image3.jpg", "url": "https://pandabuy.allapp.link/co4vus10b4mjcscn7uig"},
        {"name": "Trapster Jacket", "image": "jackets_images/image4.webp", "url": "https://pandabuy.allapp.link/co4vv6ogpf6oar2jdd4g"},
        {"name": "Canada Goose Wyndham Parka", "image": "jackets_images/image5.webp", "url": "https://pandabuy.allapp.link/co4vvr9rogtreqrk5b70"},


        {"name": "Prada Puffer Jacket", "image": "jackets_images/image6.jpg", "url": "https://pandabuy.allapp.link/co5006h0b4mjcscn7v10"},
        {"name": "Rick Own Puffer Jacket", "image": "jackets_images/image7.jpg", "url": "https://pandabuy.allapp.link/co500c0gpf6oar2jddkg"},
        {"name": "Moncler Maya Jacket", "image": "jackets_images/image8.webp", "url": "https://pandabuy.allapp.link/co500l1rogtreqrk5bh0"},
        {"name": "THE NORTH FACE 1996 Retro Nuptse Jacket", "image": "jackets_images/image9.jpg", "url": "https://pandabuy.allapp.link/co502b0gpf6oar2jdeb0"},
        {"name": "Drake Nike Jacket", "image": "jackets_images/image10.jpg", "url": "https://pandabuy.allapp.link/co502h8gpf6oar2jdef0"},

        {"name": "Kapital Puffer Vest", "image": "jackets_images/image11.avif", "url": "https://pandabuy.allapp.link/co502p9rogtreqrk5ce0"},
        {"name": "LV Varsity Jacket", "image": "jackets_images/image12.jpg", "url": "https://pandabuy.allapp.link/co504j10b4mjcscn80v0"},
        {"name": "Spider X Moncler Maya Jacket", "image": "jackets_images/image13.avif", "url": "https://pandabuy.allapp.link/co504sh0b4mjcscn814g"},
        {"name": " Balenciaga X Astronaut Jacket", "image": "jackets_images/image14.avif", "url": "https://pandabuy.allapp.link/co50539rogtreqrk5d7g"},
        {"name": "Balenciaga Cropped Fur Jacket", "image": "jackets_images/image15.jpg", "url": "https://pandabuy.allapp.link/co505jh0b4mjcscn81e0"},

        {"name": "10+ Human Made Jackets", "image": "jackets_images/image16.jpg", "url": "https://pandabuy.allapp.link/co505t10b4mjcscn81j0"},
        {"name": "Yeezy X Gap Jacket", "image": "jackets_images/image17.avif", "url": "https://pandabuy.allapp.link/co506o0gpf6oar2jdg9g"},
        {"name": "Balenciaga Track Jacket", "image": "jackets_images/image18.jpg", "url": "https://pandabuy.allapp.link/co507d10b4mjcscn82a0"},
        {"name": "Bottega Veneta Cropped Black Jacket", "image": "jackets_images/image19.jpg", "url": "https://pandabuy.allapp.link/co507kh0b4mjcscn82dg"},
        {"name": "Bape Jacket", "image": "jackets_images/image20.avif", "url": "https://pandabuy.allapp.link/co507t8gpf6oar2jdgl0"},

        {"name": "Canada Goose Expedition 4460 Jacket", "image": "jackets_images/image21.jpg", "url": "https://pandabuy.allapp.link/co5083hrogtreqrk5eqg"},
        {"name": "Chrome Heart Jacket", "image": "jackets_images/image22.jpg", "url": "https://pandabuy.allapp.link/co509mp0b4mjcscn83fg"},#
        {"name": "CPFM Weed Jacket", "image": "jackets_images/image23.avif", "url": "https://pandabuy.allapp.link/co50auh0b4mjcscn8440"},
        {"name": "Craig Green Jacket", "image": "jackets_images/image24.avif", "url": "https://pandabuy.allapp.link/co50b39rogtreqrk5g50"},
        {"name": "House of Errors Vest", "image": "jackets_images/image25.avif", "url": "https://pandabuy.allapp.link/co50b990b4mjcscn84c0"},

        {"name": "Kapital Vest", "image": "jackets_images/image26.avif", "url": "https://pandabuy.allapp.link/co50bl9rogtreqrk5gf0"},
        {"name": "Kapital Varsity Jacket", "image": "jackets_images/image27.avif", "url": "https://pandabuy.allapp.link/co50bth0b4mjcscn84q0"},
        {"name": "Kusikohc Jacket", "image": "jackets_images/image28.avif", "url": "https://pandabuy.allapp.link/co50ch8gpf6oar2jdiu0"},#dont work - wrong link
        {"name": "MKSZY Multi Cargo Jacket", "image": "jackets_images/image29.avif", "url": "https://pandabuy.allapp.link/co50ct1rogtreqrk5h6g"},
        {"name": "Needles Jacket", "image": "jackets_images/image30.avif", "url": "https://pandabuy.allapp.link/co50d4h0b4mjcscn85b0"},
        
        {"name": "Off White Laboratory of Fun Varsity Jacket", "image": "jackets_images/image31.jpg", "url": "https://pandabuy.allapp.link/co50daprogtreqrk5hbg"},
        {"name": "PAF Cross-body Zip up Fleece", "image": "jackets_images/image32.avif", "url": "https://pandabuy.allapp.link/co50dmh0b4mjcscn85k0"},
        {"name": "Palm Angels x Moncler Maya 70 Jacket", "image": "jackets_images/image33.avif", "url": "https://pandabuy.allapp.link/co50h0hrogtreqrk5j30"},
        {"name": "Rick Owens x Moncler Puffer", "image": "jackets_images/image34.jpg", "url": "https://pandabuy.allapp.link/co50h6ogpf6oar2jdl7g"},
        {"name": "Stussy Air Force Jacket", "image": "jackets_images/image35.avif", "url": "https://pandabuy.allapp.link/co50hbp0b4mjcscn87j0"},
        ]
     return render(request, 'core/jackets.html', {'product_data': product_data})


def tracksuits(request):
    product_data = [
        {"name": "Drake Nocta Tracksuit ", "image": "tracksuits_images/image1.jpg", "url": "https://pandabuy.allapp.link/co8s0lhrogtuqkqg8hfg"},
        {"name": "Corteiz Tracksuit ", "image": "tracksuits_images/image2.webp", "url": "https://pandabuy.allapp.link/co8s17vm8ngrr7tbkc00"},
        {"name": "Football Tracksuit ", "image": "tracksuits_images/image3.jpg", "url": "https://pandabuy.allapp.link/co8s1b9rogtuqkqg8i1g"},
        {"name": "SPIDER Tracksuit ", "image": "tracksuits_images/image4.jpg", "url": "https://pandabuy.allapp.link/co8s1nnm8ngrr7tbkcdg"},
        {"name": "EE Tracksuit ", "image": "tracksuits_images/image5.avif", "url": "https://pandabuy.allapp.link/co8s1qvm8ngrr7tbkcfg"},

        {"name": "Central Cee X Corteiz Tracksuit ", "image": "tracksuits_images/image6.avif", "url": "https://pandabuy.allapp.link/co8s1v0gpf6pm1slfihg"},
        {"name": "Juicy Tracksuit ", "image": "tracksuits_images/image7.jpg", "url": "https://pandabuy.allapp.link/co8s239rogtuqkqg8igg"},
        {"name": "Palm Angel Tracksuit ", "image": "tracksuits_images/image8.webp", "url": "https://pandabuy.allapp.link/co8s29ogpf6pm1slfipg"},
        {"name": "30+ Trapstar Tracksuit ", "image": "tracksuits_images/image9.jpg", "url": "https://pandabuy.allapp.link/co8s33nm8ngrr7tbkdeg"},
        {"name": "4+ Syna Tracksuit ", "image": "tracksuits_images/image10.webp", "url": "https://pandabuy.allapp.link/co8s38ogpf6pm1slfjjg"},

    ]
    return render(request, 'core/tracksuits.html', {'product_data': product_data})

def budget(request):
    product_data = [
        {"name": "NOFS Tracksuit ", "image": "budget_images/image1.jpg", "url": "https://weidian.info/58s4h"}, #dont work
        {"name": "Stussy Sweater ", "image": "budget_images/image2.jpg", "url": "https://pandabuy.allapp.link/co4vi58gpf6oar2jd5p0"},
        {"name": "LV Belt ", "image": "budget_images/image3.jpg", "url": "https://pandabuy.allapp.link/co4vic90b4mjcscn7nvg"},
        {"name": "Hermes Belt ", "image": "budget_images/image4.jpg", "url": "https://pandabuy.allapp.link/co4vij8gpf6oar2jd61g"},
        {"name": "LV Trainers ", "image": "budget_images/image5.jpg", "url": "https://pandabuy.allapp.link/co4vje9rogtreqrk5430"},#dont work

        {"name": "Iced Out Cuban Bracelet ", "image": "budget_images/image6.avif", "url": "https://pandabuy.allapp.link/co4vjnp0b4mjcscn7ol0"},
        {"name": "Cuban Bracelet ", "image": "budget_images/image7.avif", "url": "https://pandabuy.allapp.link/co4vjuprogtreqrk54e0"},
        {"name": "Rolex Watch ", "image": "budget_images/image8.jpg", "url": "https://pandabuy.allapp.link/co4vk6h0b4mjcscn7otg"},
        {"name": "Sterling Sliver Bead Bracelet ", "image": "budget_images/image9.avif", "url": "https://pandabuy.allapp.link/co4vkc8gpf6oar2jd6v0"},
        {"name": "Prada Sunglasses ", "image": "budget_images/image10.jpg", "url": "https://pandabuy.allapp.link/co4vkkogpf6oar2jd72g"},

        {"name": "ASSC Shirts", "image": "budget_images/image11.jpg", "url": "https://pandabuy.allapp.link/co4vl4progtreqrk551g"},
        {"name": "Unbranded Star Full Head Zipper ", "image": "budget_images/image12.jpg", "url": "https://pandabuy.allapp.link/co4vlbogpf6oar2jd7h0"},
        {"name": "Jordan 4s", "image": "budget_images/image13.jpg", "url": "https://pandabuy.allapp.link/co4vlh90b4mjcscn7phg"},
        {"name": "Airpod Maxes", "image": "budget_images/image14.jpg", "url": "https://pandabuy.allapp.link/co4vlnh0b4mjcscn7pm0"},
        {"name": "More Stussy Hoodies", "image": "budget_images/image15.jpg", "url": "https://pandabuy.allapp.link/co4vlu9rogtreqrk55g0"},

        {"name": "Kayne West Heartbreak Shirt", "image": "budget_images/image21.jpg", "url": "https://weidian.info/3xaa2"}, # dont work - wrong link
        {"name": "Justin Bieber Colorblind Shirt", "image": "budget_images/image22.avif", "url": "https://weidian.info/qh23b"},# dont work - wrong link
        {"name": "Kayne West I Feel Like Pablo Shirt", "image": "budget_images/image23.avif", "url": "https://weidian.info/tg8jv"},# dont work - wrong link
        {"name": "Kayne West No More Parties In LA Shirt", "image": "budget_images/image24.jpg", "url": "https://weidian.info/fzvjd"},# dont work - wrong link
        {"name": "Palm Angel Shirt", "image": "budget_images/image25.jpg", "url": "https://pandabuy.allapp.link/co4vnmggpf6oar2jd8u0"},

    ]
    return render(request, 'core/budget.html', {'product_data': product_data})

def watches(request):
    product_data = [
        {"name": "Original Claw alabaster Style Retro Y2K Watch", "image": "watches_images/image1.avif", "url": "https://pandabuy.allapp.link/co8s3q1rogtuqkqg8k00"},
        {"name": "10+ G-SHOCK Watches", "image": "watches_images/image2.jpg", "url": "https://pandabuy.allapp.link/co8s40vm8ngrr7tbke30"},
        {"name": "Cartier Crash Watch", "image": "watches_images/image3.avif", "url": "https://pandabuy.allapp.link/co8s45vm8ngrr7tbke60"},
        {"name": "Apple Watch Series 8", "image": "watches_images/image4.jpg", "url": "https://pandabuy.allapp.link/co8s49vm8ngrr7tbke8g"},
        {"name": "Apple Watch Ultra", "image": "watches_images/image5.png", "url": "https://pandabuy.allapp.link/co8s4f0gpf6pm1slfkjg"},
        
        {"name": "Rolex Daytona", "image": "watches_images/image6.jpg", "url": "https://pandabuy.allapp.link/co8s4kfm8ngrr7tbked0"},
        {"name": "Rolex Submariner", "image": "watches_images/image7.jpg", "url": "https://pandabuy.allapp.link/co8s4oogpf6pm1slfkrg"},
        {"name": "Rolex Datejust", "image": "watches_images/image8.png", "url": "https://pandabuy.allapp.link/co8s4u1rogtuqkqg8kug"},

    ]
    return render(request, 'core/watches.html', {'product_data': product_data})

def tech(request):
    product_data = [
        {"name": "Mechanical Keyboard Keycap PBT Thermal", "image": "tech_images/image1.jpg", "url": "https://pandabuy.allapp.link/co8rm38gpf6pm1slf9eg"},
        {"name": "Pharaoh Key Cap Black PBT Thermal", "image": "tech_images/image2.png", "url": "https://pandabuy.allapp.link/co8rm8progtuqkqg8a1g"},
        {"name": "CHERRY shaft MX switch", "image": "tech_images/image3.png", "url": "https://pandabuy.allapp.link/co8rmcggpf6pm1slf9m0"},
        {"name": "30+ Graphic Mouse Pads", "image": "tech_images/image4.png", "url": "https://pandabuy.allapp.link/co8rmh1rogtuqkqg8a9g"},
        {"name": "TTC keyboard shaft", "image": "tech_images/image5.png", "url": "https://pandabuy.allapp.link/co8rmm1rogtuqkqg8afg"},

        {"name": "20+ Kaws Mouse Pads", "image": "tech_images/image6.avif", "url": "https://pandabuy.allapp.link/co8rqknm8ngrr7tbk750"},
        {"name": "Playstation Control Kreeks", "image": "tech_images/image7.avif", "url": "https://pandabuy.allapp.link/co8rqonm8ngrr7tbk780"},
        {"name": "XBOX Control Kreeks", "image": "tech_images/image8.avif", "url": "https://pandabuy.allapp.link/co8rqt7m8ngrr7tbk7b0"},
        {"name": " Xbox Series Controllers", "image": "tech_images/image9.avif", "url": "https://pandabuy.allapp.link/co8rr4ogpf6pm1slfdi0"},
        {"name": "Iron Man helmet", "image": "tech_images/image10.jpg", "url": "https://pandabuy.allapp.link/co8rrb0gpf6pm1slfdq0"},

        {"name": "Airpods + Airmaxes", "image": "tech_images/image11.jpg", "url": "https://pandabuy.allapp.link/co8rrgggpf6pm1slfdu0"},
        {"name": "Bluetooth LED Strips", "image": "tech_images/image12.avif", "url": "https://pandabuy.allapp.link/co8rrtogpf6pm1slfe9g"},
        {"name": "Wireless RKG68 mechanical keyboard", "image": "tech_images/image13.avif", "url": "https://pandabuy.allapp.link/co8rs1ggpf6pm1slfec0"},
        {"name": "Keyboard + Mouse Set", "image": "tech_images/image14.avif", "url": "https://pandabuy.allapp.link/co8rs5ggpf6pm1slfee0"},
        {"name": "Customized Aviation Plug-In Cable", "image": "tech_images/image15.webp", "url": "https://pandabuy.allapp.link/co8rsf0gpf6pm1slfeng"},

        
        {"name": "Bm800 Condenser Microphone + V8 Sound Card ", "image": "tech_images/image16.avif", "url": "https://pandabuy.allapp.link/co8rsuogpf6pm1slff70"},
        {"name": "All Models Of Dyson Hair Dryers", "image": "tech_images/image17.jpg", "url": "https://pandabuy.allapp.link/co8rt4fm8ngrr7tbk8r0"},
        {"name": "Replica XBOX Controllers", "image": "tech_images/image18.avif", "url": "https://pandabuy.allapp.link/co8rt8vm8ngrr7tbk8vg"},
        {"name": "GOPRO7/8/9/MAX Nikon Key 170 Motion CCD Digital Camera", "image": "tech_images/image19.avif", "url": "https://pandabuy.allapp.link/co8rteogpf6pm1slffm0"},
        {"name": "Skullcandy Crusher Headphones", "image": "tech_images/image20.avif", "url": "https://pandabuy.allapp.link/co8rtjogpf6pm1slffog"},

        {"name": "Beats studio Wireless Headphones", "image": "tech_images/image21.png", "url": "https://weidian.info/97m2j"},#dont work
        {"name": "JBL Flip 6", "image": "tech_images/image22.jpg", "url": "https://pandabuy.allapp.link/co8rttnm8ngrr7tbk9h0"},
        {"name": "Multifunctional 25 In 1 Precision Manual Screwdriver Set", "image": "tech_images/image23.avif", "url": "https://pandabuy.allapp.link/co8ru2vm8ngrr7tbk9n0"},
        {"name": "Dyson Vacuum Cleaner V7s Four In One Handheld", "image": "tech_images/image24.jpg", "url": "https://pandabuy.allapp.link/co8ru6progtuqkqg8fm0"},
        {"name": " Silicone Self-adhesive Wire Organizer Combination", "image": "tech_images/image25.jpg", "url": "https://pandabuy.allapp.link/co8rua1rogtuqkqg8fpg"},

        {"name": "Top Quality Air Maxes", "image": "tech_images/image26.jpg", "url": "https://pandabuy.allapp.link/coa0us9rogtuqkqgr930"},
        {"name": "Top Quality 15w Charger", "image": "tech_images/image27.jpg", "url": "https://pandabuy.allapp.link/coa0vfvm8ngrr7tc70l0"},
        {"name": "Top Quality Airpod 2 Pro USB-C", "image": "tech_images/image28.jpg", "url": "https://pandabuy.allapp.link/coa0voprogtuqkqgr9fg"},
        {"name": "Top Quality Airpod 3", "image": "tech_images/image29.jpg", "url": "https://pandabuy.allapp.link/coa1009rogtuqkqgr9i0"},
        {"name": "Top Quality Airpod 2 Pro with ANC", "image": "tech_images/image30.jpg", "url": "https://pandabuy.allapp.link/coa108vm8ngrr7tc712g"},

         {"name": "Top Quality JBL Flip 6", "image": "tech_images/image31.jpg", "url": "https://pandabuy.allapp.link/coa1n690b4mo6u3l0j9g"},
        {"name": "Top Quality JBL Pulse 6", "image": "tech_images/image32.jpg", "url": "https://pandabuy.allapp.link/coa1n91rogtuqkqgrl80"},
        {"name": "Top Quality J Tour Pro 2", "image": "tech_images/image33.jpg", "url": "https://pandabuy.allapp.link/coa1ns0gpf6pm1sm2lb0"},
        {"name": "Top Quality Apple Pencil 2", "image": "tech_images/image34.jpg", "url": "https://pandabuy.allapp.link/coa1n29rogtuqkqgrl60"},
        {"name": "Top Quality Battery Pack", "image": "tech_images/image35.jpg", "url": "https://pandabuy.allapp.link/coa1ncta5kl9e2knmc70"},

        {"name": "Top Quality Galaxy Buds 2 Pro", "image": "tech_images/image36.jpg", "url": "https://pandabuy.allapp.link/coa22oogpf6pm1sm2qrg"},
        {"name": "Top Quality Dyson Airwarp HS05", "image": "tech_images/image37.jpg", "url": "https://pandabuy.allapp.link/coa22qprogtuqkqgrr7g"},
        {"name": "Top Quality Iphone 15 Pro Max", "image": "tech_images/image38.jpg", "url": "https://pandabuy.allapp.link/coa22togpf6pm1sm2qtg"},
        {"name": "Top Quality Galaxy S24 Ultra", "image": "tech_images/image39.jpg", "url": "https://pandabuy.allapp.link/coa230la5kl9e2knmi70"},
        {"name": "Top Quality  Iphone 14 Pro Max", "image": "tech_images/image40.jpg", "url": "https://pandabuy.allapp.link/coa232ta5kl9e2knmi80"},

        {"name": "Top Quality Dyson Airwarp HS01", "image": "tech_images/image41.jpg", "url": "https://pandabuy.allapp.link/coa2bj8gpf6pm1sm2v1g"},
        {"name": "Top Quality Galaxy S23 Ultra", "image": "tech_images/image42.jpg", "url": "https://pandabuy.allapp.link/coa2bs1rogtuqkqgs020"},
        {"name": "Top Quality Air Max (Metal case)", "image": "tech_images/image43.jpg", "url": "https://pandabuy.allapp.link/coa2buvm8ngrr7tc7n7g"},
        {"name": "Top Quality Dyson hairdryer HD08", "image": "tech_images/image44.jpg", "url": "https://pandabuy.allapp.link/coa2c0h0b4mo6u3l0ue0"},
        {"name": "Top Quality Dyson HD15 Hairdryer", "image": "tech_images/image45.jpg", "url": "https://pandabuy.allapp.link/coa2c3da5kl9e2knmnc0"},

        {"name": "Top Quality Dyson HD07", "image": "tech_images/image46.jpg", "url": "https://pandabuy.allapp.link/coa2ke8gpf6pm1sm3470"},
        {"name": "Top Quality G&H&D hair Straightener", "image": "tech_images/image47.jpg", "url": "https://pandabuy.allapp.link/coa2klta5kl9e2knmsag"},
        {"name": "Top Quality Apple Ultra 2", "image": "tech_images/image48.png", "url": "https://pandabuy.allapp.link/coa2kt8gpf6pm1sm34fg"},
        {"name": "Top Quality Apple Hermes S8 Watch", "image": "tech_images/image49.jpg", "url": "https://pandabuy.allapp.link/coa2l57m8ngrr7tc7seg"},
        {"name": "Top Quality GHD V Gold", "image": "tech_images/image50.jpg", "url": "https://pandabuy.allapp.link/coa2ld10b4mo6u3l13h0"},

        {"name": "Top Quality Apple Watch S9", "image": "tech_images/image51.jpg", "url": "https://pandabuy.allapp.link/coa2ur90b4mo6u3l19e0"},
        {"name": "Top Quality JBL Pulse 5", "image": "tech_images/image52.jpg", "url": "https://pandabuy.allapp.link/coa2up90b4mo6u3l19cg"},
        {"name": "Top Quality PS5 Controllers", "image": "tech_images/image53.jpg", "url": "https://pandabuy.allapp.link/coa2umhrogtuqkqgsadg"},
        {"name": "Top Quality JBL Flip 6", "image": "tech_images/image54.jpg", "url": "https://pandabuy.allapp.link/coa2uk0gpf6pm1sm3aig"},
        {"name": "Top Quality Galaxy Buds FE", "image": "tech_images/image55.jpg", "url": "https://pandabuy.allapp.link/coa2uhvm8ngrr7tc822g"},

        {"name": "Top Quality Airpods 2", "image": "tech_images/image56.jpg", "url": "https://pandabuy.allapp.link/coa2ufh0b4mo6u3l196g"},
        
    ]
    return render(request, 'core/tech.html', {'product_data': product_data})