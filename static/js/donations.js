$(document).ready(function() {
    $('.chart').easyPieChart({
        easing: 'easeOutElastic',
        delay: 3000,
        barColor: '#26B99A',
        trackColor: '#fff',
        scaleColor: false,
        lineWidth: 20,
        trackWidth: 16,
        lineCap: 'butt',
        onStep: function(from, to, percent) {
            $(this.el).find('.percent').text(Math.round(percent));
        }
    });
});