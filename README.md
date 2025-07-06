# 🚀 LeadFlow AI - Plateforme de Qualification Automatique des Leads

**Automatisez la qualification et le scoring de vos leads avec l'IA. Augmentez vos conversions de 300% avec notre plateforme intelligente.**

[![Next.js](https://img.shields.io/badge/Next.js-14-black?style=for-the-badge&logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.3-blue?style=for-the-badge&logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.3-38B2AC?style=for-the-badge&logo=tailwind-css)](https://tailwindcss.com/)
[![Prisma](https://img.shields.io/badge/Prisma-5.7-2D3748?style=for-the-badge&logo=prisma)](https://www.prisma.io/)

## 🎯 Vue d'ensemble

LeadFlow AI est une plateforme SaaS moderne qui révolutionne la qualification de leads grâce à l'intelligence artificielle. Notre solution permet aux entreprises de :

- **Qualifier automatiquement** leurs leads en 30 secondes
- **Scorer les prospects** avec une précision de 95%
- **Augmenter les conversions** de 300%
- **Automatiser le nurturing** des prospects
- **Intégrer facilement** avec les CRM existants

## ✨ Fonctionnalités Principales

### 🤖 IA Prédictive Avancée
- Analyse de plus de 50 critères de qualification
- Scoring automatique en temps réel
- Apprentissage continu pour améliorer la précision

### ⚡ Qualification Automatique
- Traitement des leads en 30 secondes
- Pas d'intervention manuelle requise
- Workflows personnalisables

### 📊 Analytics en Temps Réel
- Tableaux de bord détaillés
- Rapports automatisés
- Métriques de performance

### 🔗 Intégrations Native
- HubSpot, Salesforce, Pipedrive
- 50+ autres outils CRM
- API REST complète

### 🛡️ Sécurité Enterprise
- Chiffrement de niveau bancaire
- Conformité GDPR
- Authentification multi-facteurs

## 🛠️ Stack Technique

### Frontend
- **Next.js 14** - Framework React moderne
- **TypeScript** - Typage statique
- **TailwindCSS** - Framework CSS utilitaire
- **Framer Motion** - Animations fluides
- **Lucide React** - Icônes modernes

### Backend
- **Next.js API Routes** - API backend
- **Prisma** - ORM moderne
- **PostgreSQL** - Base de données relationnelle
- **NextAuth.js** - Authentification

### Services Externes
- **OpenAI** - Intelligence artificielle
- **Stripe** - Paiements
- **Resend** - Emails transactionnels
- **Vercel** - Déploiement

## 🚀 Installation Rapide

### Prérequis
- Node.js 18+ 
- PostgreSQL 12+
- npm ou yarn

### 1. Cloner le projet
```bash
git clone https://github.com/votre-username/leadflow-ai.git
cd leadflow-ai
```

### 2. Installer les dépendances
```bash
npm install
# ou
yarn install
```

### 3. Configuration de l'environnement
```bash
cp env.example .env.local
```

Éditez `.env.local` avec vos clés API :
```env
# Database
DATABASE_URL="postgresql://username:password@localhost:5432/leadflow_ai"

# NextAuth.js
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="your-secret-key"

# OpenAI
OPENAI_API_KEY="your-openai-api-key"

# Stripe
STRIPE_PUBLISHABLE_KEY="pk_test_..."
STRIPE_SECRET_KEY="sk_test_..."

# Email
RESEND_API_KEY="your-resend-api-key"
```

### 4. Configuration de la base de données
```bash
# Générer le client Prisma
npx prisma generate

# Créer les tables
npx prisma db push

# (Optionnel) Seeder avec des données de test
npx prisma db seed
```

### 5. Lancer le serveur de développement
```bash
npm run dev
# ou
yarn dev
```

Ouvrez [http://localhost:3000](http://localhost:3000) dans votre navigateur.

## 📁 Structure du Projet

```
leadflow-ai/
├── src/
│   ├── app/                 # App Router Next.js 14
│   │   ├── globals.css      # Styles globaux
│   │   ├── layout.tsx       # Layout principal
│   │   └── page.tsx         # Page d'accueil
│   ├── components/          # Composants React
│   │   ├── ui/             # Composants UI réutilisables
│   │   ├── forms/          # Formulaires
│   │   ├── dashboard/      # Composants dashboard
│   │   └── marketing/      # Composants marketing
│   ├── lib/                # Utilitaires et configurations
│   │   ├── prisma.ts       # Client Prisma
│   │   ├── auth.ts         # Configuration NextAuth
│   │   ├── stripe.ts       # Configuration Stripe
│   │   └── utils.ts        # Fonctions utilitaires
│   ├── types/              # Types TypeScript
│   ├── hooks/              # Hooks React personnalisés
│   └── styles/             # Styles additionnels
├── prisma/                 # Schéma et migrations
├── public/                 # Assets statiques
├── docs/                   # Documentation
└── scripts/                # Scripts utilitaires
```

## 🎨 Design System

LeadFlow AI utilise un design system moderne avec :

- **Couleurs principales** : Bleu LeadFlow (#0ea5e9)
- **Typographie** : Inter (Google Fonts)
- **Composants** : Radix UI + TailwindCSS
- **Animations** : Framer Motion
- **Responsive** : Mobile-first design

### Classes CSS personnalisées
```css
.btn-primary    /* Bouton principal */
.btn-secondary  /* Bouton secondaire */
.card          /* Carte avec ombre */
.text-gradient /* Texte avec dégradé */
.glass-effect  /* Effet de verre */
```

## 🔧 Configuration Avancée

### Base de données
```bash
# Voir les migrations
npx prisma migrate status

# Créer une nouvelle migration
npx prisma migrate dev --name add_new_feature

# Réinitialiser la base de données
npx prisma migrate reset
```

### Variables d'environnement
```env
# Production
NODE_ENV=production
DATABASE_URL="postgresql://..."
NEXTAUTH_URL="https://votre-domaine.com"

# Développement
NODE_ENV=development
DATABASE_URL="postgresql://localhost:5432/leadflow_ai_dev"
```

### Déploiement
```bash
# Build de production
npm run build

# Vérification des types
npm run type-check

# Linting
npm run lint
```

## 📊 Fonctionnalités Détaillées

### 1. Qualification IA
- **Analyse comportementale** : Pages visitées, temps passé
- **Données démographiques** : Taille d'entreprise, secteur
- **Intent signals** : Recherches, téléchargements
- **Scoring prédictif** : Probabilité de conversion

### 2. Nurturing Automatique
- **Séquences d'email** personnalisées
- **Triggers intelligents** basés sur le comportement
- **A/B testing** automatique
- **Optimisation continue** des performances

### 3. Intégrations
- **HubSpot** : Synchronisation bidirectionnelle
- **Salesforce** : Import/export des leads
- **Pipedrive** : Gestion des pipelines
- **Zapier** : Automatisations personnalisées

### 4. Analytics
- **Tableaux de bord** en temps réel
- **Rapports automatisés** hebdomadaires/mensuels
- **ROI tracking** détaillé
- **Prédictions** de performance

## 🚀 Déploiement

### Vercel (Recommandé)
1. Connectez votre repo GitHub à Vercel
2. Configurez les variables d'environnement
3. Déployez automatiquement

### Railway
1. Créez un projet Railway
2. Connectez votre repo
3. Configurez PostgreSQL et les variables

### Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

## 📈 Métriques et Performance

- **Temps de chargement** : < 2 secondes
- **Score Lighthouse** : 95+
- **SEO** : Optimisé pour les moteurs de recherche
- **Accessibilité** : WCAG 2.1 AA
- **Mobile** : Responsive design

## 🔒 Sécurité

- **Authentification** : NextAuth.js avec OAuth
- **Autorisation** : Rôles et permissions
- **Chiffrement** : HTTPS, données chiffrées
- **GDPR** : Conformité européenne
- **Audit** : Logs de sécurité

## 🤝 Contribution

1. Fork le projet
2. Créez une branche feature (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Standards de code
- **TypeScript** strict mode
- **ESLint** + **Prettier**
- **Tests** unitaires et d'intégration
- **Documentation** des APIs

## 📞 Support

- **Documentation** : [docs.leadflow-ai.com](https://docs.leadflow-ai.com)
- **Email** : support@leadflow-ai.com
- **Discord** : [discord.gg/leadflow](https://discord.gg/leadflow)
- **Twitter** : [@leadflow_ai](https://twitter.com/leadflow_ai)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- [Next.js](https://nextjs.org/) - Framework React
- [TailwindCSS](https://tailwindcss.com/) - Framework CSS
- [Prisma](https://www.prisma.io/) - ORM moderne
- [OpenAI](https://openai.com/) - Intelligence artificielle
- [Vercel](https://vercel.com/) - Plateforme de déploiement

---

**LeadFlow AI** - Transformez vos ventes avec l'IA 🚀 