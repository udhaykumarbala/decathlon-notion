# loop through the folders in the directory
import os


htmlTemplateStart = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>CodePen - Full-Screen Responsive Image Slider</title>
  <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css'>
  <link rel="stylesheet" href="./style.css">
<style>
  @import url("https://fonts.googleapis.com/css2?family=Lexend:wght@400;700&display=swap");

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: "Lexend", sans-serif;
  background-color: #362a2b;
  color: #e5ebf3;
}

.slider {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}

.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.4s ease-in-out;
}

.slide.current {
  opacity: 1;
}


.slide:first-child {
  background: url("1.png") no-repeat
    center top/cover;
}

.slide:nth-child(2) {
  background: url("2.png") no-repeat
    center top/cover;
}

.slide:nth-child(3) {
  background: url("3.png") no-repeat
    center top/cover;
}

.slide:nth-child(4) {
  background: url("4.png") no-repeat
    center top/cover;
}

.slide:nth-child(5) {
  background: url("5.png") no-repeat
    center top/cover;
}

.slide:nth-child(6) {
  background: url("6.png") no-repeat
    center top/cover;
}

.slide:nth-child(7) {
  background: url("7.png") no-repeat
    center top/cover;
}

.slide:nth-child(8) {
  background: url("8.png") no-repeat
    center top/cover;
}

.slide:nth-child(9) {
  background: url("9.png") no-repeat
    center top/cover;
}

.slide:nth-child(10) {
  background: url("10.png") no-repeat
    center top/cover;
}

.slide:nth-child(11) {
  background: url("11.png") no-repeat
    center top/cover;
}

.slide:nth-child(12) {
  background: url("12.png") no-repeat
    center top/cover;
}

.slide:nth-child(13) {
  background: url("13.png") no-repeat
    center top/cover;
}

.slide:nth-child(14) {
  background: url("14.png") no-repeat
    center top/cover;
}

.slide:nth-child(15) {
  background: url("15.png") no-repeat
    center top/cover;
}

.slide:nth-child(16) {
  background: url("16.png") no-repeat
    center top/cover;
}

.slide:nth-child(17) {
  background: url("17.png") no-repeat
    center top/cover;
}

.slide:nth-child(18) {
  background: url("18.png") no-repeat
    center top/cover;
}

.slide:nth-child(19) {
  background: url("19.png") no-repeat
    center top/cover;
}

.slide:nth-child(20) {
  background: url("20.png") no-repeat
    center top/cover;
}

.slide:nth-child(21) {
  background: url("21.png") no-repeat
    center top/cover;
}

.slide:nth-child(22) {
  background: url("22.png") no-repeat
    center top/cover;
}

.slide:nth-child(23) {
  background: url("23.png") no-repeat
    center top/cover;
}

.slide:nth-child(24) {
  background: url("24.png") no-repeat
    center top/cover;
}

.slide:nth-child(25) {
  background: url("25.png") no-repeat
    center top/cover;
}

.buttons button#prev {
  position: absolute;
  top: 50%;
  left: 1rem;
}

.buttons button#next {
  position: absolute;
  top: 50%;
  right: 1rem;
}

.buttons button {
  border: 2px solid #e5ebf3;
  background-color: transparent;
  color: #e5ebf3;
  cursor: pointer;
  padding: 13px 15px;
  border-radius: 50%;
  outline: none;
}

.buttons button:hover {
  background-color: #e5ebf3;
  color: #362a2b;
}

@media (min-width: 640px) and (min-height: 640px) {
  .slide .content {
    bottom: 70px;
    left: -600px;
    width: 600px;
    padding: 2rem;
    line-height: 1.6;
  }

  .slide .content h1 {
    font-size: 2rem;
  }

  .slide.current .content {
    transform: translateX(600px);
  }
}
</style>
</head>

<body>
  <!-- partial:index.partial.html -->
  <div class="slider">
    <div class="slide current"></div>"""
    

htmlTemplateEnd = """

    </div>
  <div class="buttons">
    <button id="prev"><i class="fas fa-arrow-left"></i></button>
    <button id="next"><i class="fas fa-arrow-right"></i></button>
  </div>
  <!-- partial -->
  <script>
    const slides = document.querySelectorAll(".slide");
    const nextButton = document.getElementById("next");
    const prevButton = document.getElementById("prev");
    const auto = true;
    const intervalTime = 5000;
    let slideInterval;

    const nextSlide = () => {
      const current = document.querySelector(".current");
      current.classList.remove("current");
      if (current.nextElementSibling) {
        current.nextElementSibling.classList.add("current");
      } else {
        slides[0].classList.add("current");
      }
    };

    const prevSlide = () => {
      const current = document.querySelector(".current");
      current.classList.remove("current");
      if (current.previousElementSibling) {
        current.previousElementSibling.classList.add("current");
      } else {
        slides[slides.length - 1].classList.add("current");
      }
    };

    nextButton.addEventListener("click", () => {
      nextSlide();
      if (auto) {
        clearInterval(slideInterval);
        slideInterval = setInterval(nextSlide, intervalTime);
      }
    });
    prevButton.addEventListener("click", () => {
      prevSlide();
      if (auto) {
        clearInterval(slideInterval);
        slideInterval = setInterval(nextSlide, intervalTime);
      }
    });

    if (auto) {
      slideInterval = setInterval(nextSlide, intervalTime);
    }

  </script>

</body>

</html>"""
for folder in os.listdir():
    # check if the folder is a directory
    if os.path.isdir(os.path.join(folder)):
        # loop through the files in the folder
        count = 0
        for file in os.listdir(os.path.join(folder)):
            # check if the file is a file
            print(file)
            if os.path.isfile(os.path.join(folder, file)):
                # check if the file is a .txt file
                if file.endswith('.png'):
                    num = int(file.split('.')[0])
                    print(num)
                    if num > count:
                        count = num
                        print("count",count)
        print("final",count)
        # create a index.html file in the folder
        with open(os.path.join(folder, 'index.html'), 'w') as f:
            template = htmlTemplateStart
            for i in range(1, count):
                template += """
    <div class="slide"></div>"""
            template += htmlTemplateEnd
            f.write(template)
