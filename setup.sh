#!/bin/bash

echo "🚀 Configuration de LeadFlow AI..."
echo "=================================="

# Vérifier si Node.js est installé
if ! command -v node &> /dev/null; then
    echo "❌ Node.js n'est pas installé. Veuillez installer Node.js 18+"
    exit 1
fi

# Vérifier la version de Node.js
NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "❌ Node.js 18+ est requis. Version actuelle: $(node -v)"
    exit 1
fi

echo "✅ Node.js $(node -v) détecté"

# Installer les dépendances
echo "📦 Installation des dépendances..."
npm install

if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de l'installation des dépendances"
    exit 1
fi

echo "✅ Dépendances installées"

# Copier le fichier d'environnement
if [ ! -f .env.local ]; then
    echo "🔧 Configuration de l'environnement..."
    cp env.example .env.local
    echo "✅ Fichier .env.local créé"
    echo "⚠️  N'oubliez pas de configurer vos variables d'environnement dans .env.local"
else
    echo "✅ Fichier .env.local existe déjà"
fi

# Générer le client Prisma
echo "🗄️  Configuration de la base de données..."
npx prisma generate

if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de la génération du client Prisma"
    exit 1
fi

echo "✅ Client Prisma généré"

# Vérifier la configuration TypeScript
echo "🔍 Vérification de la configuration TypeScript..."
npx tsc --noEmit

if [ $? -ne 0 ]; then
    echo "⚠️  Avertissements TypeScript détectés (non bloquants)"
else
    echo "✅ Configuration TypeScript OK"
fi

echo ""
echo "🎉 Configuration terminée !"
echo "=========================="
echo ""
echo "📋 Prochaines étapes :"
echo "1. Configurez votre base de données PostgreSQL"
echo "2. Modifiez .env.local avec vos clés API"
echo "3. Lancez le serveur : npm run dev"
echo "4. Ouvrez http://localhost:3000"
echo ""
echo "📚 Documentation : README.md"
echo "📋 TODO : TODO.md"
echo "🎯 Stratégie : MARKETING_STRATEGY.md" 