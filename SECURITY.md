# SECURITY GUIDE - READ THIS BEFORE PUSHING TO GIT

## 🚨 CRITICAL: Never Commit API Keys!

### What NOT to do:
- ❌ Never put real API keys in your code
- ❌ Never commit .env files with real credentials
- ❌ Never share API keys in chat/email/documentation
- ❌ Never put credentials in README files

### What TO do:
- ✅ Use .env files for local development
- ✅ Use environment variables in production
- ✅ Use template files (.env.template) for examples
- ✅ Add .env to .gitignore
- ✅ Use secret management services for production

## 🔐 Safe Repository Setup:

1. **Create your .env file locally:**
   ```bash
   cp env.template .env
   # Edit .env with your REAL credentials
   ```

2. **Verify .gitignore includes .env:**
   ```bash
   cat .gitignore | grep "\.env"
   ```

3. **Before committing, check what you're adding:**
   ```bash
   git status
   git diff --cached
   ```

4. **Never commit these files:**
   - `.env`
   - `.env.local`
   - `.env.production`
   - Any file containing real API keys

## 🛡️ Production Deployment:

### For Cloud Platforms:
- **Heroku**: Use `heroku config:set KEY=value`
- **AWS**: Use AWS Secrets Manager
- **Google Cloud**: Use Secret Manager
- **Azure**: Use Key Vault

### For VPS/Docker:
- Use environment variables in docker-compose.yml
- Use secret files mounted as volumes
- Never put secrets in Docker images

## 🔍 Security Checklist:

Before pushing to any repository:
- [ ] No .env files in git status
- [ ] No API keys in code files
- [ ] No credentials in README/docs
- [ ] .gitignore includes .env
- [ ] Template files use placeholder values

## 🚨 If You Accidentally Commit Secrets:

1. **Immediately revoke the exposed credentials**
2. **Remove from git history:**
   ```bash
   git filter-branch --force --index-filter \
   'git rm --cached --ignore-unmatch .env' \
   --prune-empty --tag-name-filter cat -- --all
   ```
3. **Force push to update remote:**
   ```bash
   git push origin --force --all
   ```
4. **Regenerate all exposed credentials**

## 📞 Emergency Response:

If you've exposed credentials:
1. **Immediately revoke them** in the respective service
2. **Generate new credentials**
3. **Update all systems** using the old credentials
4. **Monitor for unauthorized usage**

Remember: **Security is everyone's responsibility!**
