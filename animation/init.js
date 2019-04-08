requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            functions: {
                js: 'checkPangram',
                python: 'check_pangram'
            }
        });
        io.start();
    }
);