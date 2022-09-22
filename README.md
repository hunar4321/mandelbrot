# Mandelbrot
Simple Mandelbrot in javascript
Note: The canonical way to code Mandelbrot is to use complex number which results in a more elegant equation, however, this will require using an external library and also introduction to complex numbers which overall makes the video longer and harder to follow.
'''
  <canvas id="gardun" width="1000" height="1000"></canvas>
  <script>
  m = document.getElementById("gardun").getContext("2d")
  atom = function(x,y,c){m.fillStyle=c; m.fillRect(x,y,3,3)}
  for(y=1; y<1000; y++){
  for(x=1; x<1000; x++){
  dx = (x-500)/2000-0.12
  dy = (y-500)/2000-0.82
  a = dx
  b = dy
  for(t=1; t<200; t++){
  d = (a*a)-(b*b)+dx
  b = 2*(a*b)+dy
  a = d
  H = d>200
  if(H){atom(x,y,"rgb("+ t*3 +","+ t +","+ t*0.5 +")"); break}
  }}}
  </script>
'''

![](mendlbort.JPG)
