import fs from 'fs';
import path from 'path';
import { google } from 'googleapis';
import readline from 'readline';

const SCOPES = [
  'https://www.googleapis.com/auth/documents',
  'https://www.googleapis.com/auth/drive.file'
];

const TOKEN_PATH = path.join(__dirname, 'token.json');
const CREDENTIALS_PATH = path.join(__dirname, 'client_secret.json');

/**
 * Get and store OAuth2 credentials
 * @returns {Promise<OAuth2Client>}
 */
async function getAuth() {
  // Check if credentials file exists
  if (!fs.existsSync(CREDENTIALS_PATH)) {
    throw new Error(
      `client_secret.json not found!\n\n` +
      `Please follow the setup instructions in SETUP.md to:\n` +
      `1. Create a Google Cloud project\n` +
      `2. Enable Google Docs and Drive APIs\n` +
      `3. Create OAuth credentials\n` +
      `4. Download client_secret.json to this directory`
    );
  }

  const credentials = JSON.parse(fs.readFileSync(CREDENTIALS_PATH, 'utf8'));
  const { client_secret, client_id, redirect_uris } = credentials.installed;

  const oAuth2Client = new google.auth.OAuth2(
    client_id,
    client_secret,
    redirect_uris[0]
  );

  // Check if we already have a token stored
  if (fs.existsSync(TOKEN_PATH)) {
    const token = JSON.parse(fs.readFileSync(TOKEN_PATH, 'utf8'));
    oAuth2Client.setCredentials(token);
    return oAuth2Client;
  }

  // Need to get new token
  return getNewToken(oAuth2Client);
}

/**
 * Get new OAuth token via authorization flow
 * @param {OAuth2Client} oAuth2Client
 * @returns {Promise<OAuth2Client>}
 */
async function getNewToken(oAuth2Client) {
  const authUrl = oAuth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: SCOPES,
  });

  console.log('\n=== FIRST TIME SETUP ===');
  console.log('Authorize this app by visiting this URL:\n');
  console.log(authUrl);
  console.log('\n');

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const code = await new Promise((resolve) => {
    rl.question('Enter the authorization code from the browser: ', (answer) => {
      resolve(answer);
    });
  });
  rl.close();

  try {
    const { tokens } = await oAuth2Client.getToken(code);
    oAuth2Client.setCredentials(tokens);

    // Store the token for future use
    fs.writeFileSync(TOKEN_PATH, JSON.stringify(tokens, null, 2));
    console.log('\n✓ Token stored successfully to', TOKEN_PATH);
    console.log('✓ Future runs will use this token automatically\n');

    return oAuth2Client;
  } catch (err) {
    throw new Error(`Error retrieving access token: ${err.message}`);
  }
}

export { getAuth };
