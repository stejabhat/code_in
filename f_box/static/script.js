document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('todo-form');
    
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const title = form.querySelector('input[name="title"]').value;
            const description = form.querySelector('textarea[name="description"]').value;
            
            if (title && description) {
                const newTodo = {
                    title: title,
                    description: description,
                };
                
                console.log('Form submitted', newTodo);
                
                window.location.href = '/todos/';
            }
        });
    }
});
