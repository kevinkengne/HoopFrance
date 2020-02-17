$(document).ready(function () {

    $('main').on('click', 'article', function() {
        var id = $(this).attr('data-key');
        console.log(id);
        mainVid(id);

    });

    function mainVid(id) {
        $('#video').html(`
            <iframe 
                width="800px" 
                height="450px"; 
                src="https://www.youtube.com/embed/${id}" 
                frameborder="0" 
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
            </iframe>
        `);
    }
});