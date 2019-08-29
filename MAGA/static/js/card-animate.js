window.onload = function(){
  d3.selectAll(".flip-card")
    .on("click", function(d){
      d3.selectAll(".flip-card").transition()
      .duration(200)
      .attr("opacity", 0.3)
    d3.select(this)
      .attr("opacity", 1)
      console.log("work")
    })
}
