Title: Sage Math Tool
Date: 2016-06-05
Modified: 
Category: Tools
Tags: python, Sage, Math
Slug: sage-embed
Authors: Neal Gordon
Summary: Interactive Sage Cell


<script src="https://sagecell.sagemath.org/static/jquery.min.js"></script>
<script src="https://sagecell.sagemath.org/static/embedded_sagecell.js"></script>
<script>sagecell.makeSagecell({"inputLocation": ".sage"});</script>
<link rel="stylesheet" type="text/css" href="https://sagecell.sagemath.org/static/sagecell_embed.css">
<div class="sage">
  <script type="text/x-sage">x = var('x') ; parametric_plot((cos(x),sin(x)^3),(x,0,2*pi),rgbcolor=hue(0.6))</script>
</div>
