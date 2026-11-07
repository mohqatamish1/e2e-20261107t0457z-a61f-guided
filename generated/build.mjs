import fs from 'node:fs';fs.writeFileSync('public-url.txt',process.env.NEXT_PUBLIC_API_URL || 'https://example.invalid');
