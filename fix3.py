with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace block around line 489
target = """        let initializeApp, getAuth, signInAnonymously, onAuthStateChanged, signInWithCustomToken, getFirestore, doc, setDoc, getDoc, onSnapshot, updateDoc, collection, addDoc, deleteDoc, runTransaction, arrayUnion, arrayRemove, query, orderBy, limit, serverTimestamp, where, getDocs, writeBatch;

            const providedConfig = { apiKey: "AIzaSyCbw8MNh616_OIBfoyh2gIhQQhsgsN8rAc","""

replacement = """        let initializeApp, getAuth, signInAnonymously, onAuthStateChanged, signInWithCustomToken, getFirestore, doc, setDoc, getDoc, onSnapshot, updateDoc, collection, addDoc, deleteDoc, runTransaction, arrayUnion, arrayRemove, query, orderBy, limit, serverTimestamp, where, getDocs, writeBatch;
        let auth, db, app;

        const initApp = () => {
            const api = window.firebaseAPI;
            if (!api) return console.warn("Firebase API not available yet.");
            initializeApp = api.initializeApp; getAuth = api.getAuth; signInAnonymously = api.signInAnonymously;
            onAuthStateChanged = api.onAuthStateChanged; signInWithCustomToken = api.signInWithCustomToken;
            getFirestore = api.getFirestore; doc = api.doc; setDoc = api.setDoc; getDoc = api.getDoc;
            onSnapshot = api.onSnapshot; updateDoc = api.updateDoc; collection = api.collection;
            addDoc = api.addDoc; deleteDoc = api.deleteDoc; runTransaction = api.runTransaction;
            arrayUnion = api.arrayUnion; arrayRemove = api.arrayRemove; query = api.query;
            orderBy = api.orderBy; limit = api.limit; serverTimestamp = api.serverTimestamp;
            where = api.where; getDocs = api.getDocs; writeBatch = api.writeBatch;

            const providedConfig = { apiKey: "AIzaSyCbw8MNh616_OIBfoyh2gIhQQhsgsN8rAc","""

text = text.replace(target, replacement)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
