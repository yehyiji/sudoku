// 1. firebase-ready timeout
        if (window.firebaseAPI) {
            initApp();
            renderApp();
        } else {
            const forceRenderTimeout = setTimeout(() => {
                if (!window.firebaseAPI) console.warn("Firebase not loaded yet, starting offline mode");
                initApp();
                renderApp();
            }, 2000);
            window.addEventListener('firebase-ready', () => {
                clearTimeout(forceRenderTimeout);
                initApp();
                renderApp();
            });
        }
    </script>
