var width = 1000,
    height = 600;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-120)
    .linkDistance(30)
    .size([width, height]);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

var force = d3.layout.force()
    .gravity(.03)
    .distance(200)
    .charge(-200)
    .size([width, height]);

d3.json("data.json", function(error, graph) {
    if (error) {
      console.error(error);
    }

    force.nodes(graph.nodes);
    force.links(graph.links);
    force.start();

    var link = svg.selectAll(".link")
        .data(graph.links)
        .enter().append("line")
        .attr("class", "link");

    var node = svg.selectAll(".node")
        .data(graph.nodes)
        .enter().append("g")
        .attr("class", "node")
        .style("fill", function(d) {
            console.log(color(d.weight*5));
            return color(d.weight);
        })
        .attr("r",6)
        .call(force.drag);
    
    node.append("circle")
        .attr("r", 10);
    
    node.append("text").attr("dx", 12).attr("dy", ".35em").text(function(d) { 
        return d.id 
    });
    
    force.on("tick", function() {
        link.attr("x1", function(d) { 
            return d.source.x; 
        });
        link.attr("y1", function(d) {
            return d.source.y; 
        });
        link.attr("x2", function(d) {
            return d.target.x;
        });
        link.attr("y2", function(d) {
            return d.target.y;
        });
        node.attr("transform", function(d) { 
            return "translate(" + d.x + "," + d.y + ")"; 
        });
    });
    
});
