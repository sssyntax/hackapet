// api/add-email.js
import Airtable from 'airtable';

const base = new Airtable({ apiKey: process.env.AIRTABLE_API_KEY }).base(process.env.HACKAPET_BASE_ID);

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { email } = req.body;

    // Basic validation
    if (!email || !/\S+@\S+\.\S+/.test(email)) {
      return res.status(400).json({ message: 'Invalid email format.' });
    }

    try {
      // Check if the email already exists in Airtable
      const records = await base(process.env.HACKAPET_TABLE_ID)
        .select({
          filterByFormula: `{email} = "${email}"`,
          maxRecords: 1,
        })
        .firstPage();

      if (records.length > 0) {
        return res.status(400).json({ message: 'Email already exists' });
      }

      // Add the email to Airtable
      await base(process.env.HACKAPET_TABLE_ID).create([{ fields: { email } }]);

      return res.status(200).json({ message: 'Email successfully added!' });
    } catch (error) {
      console.error('Error interacting with Airtable:', error);
      return res.status(500).json({ message: 'Error adding email. Please try again later.' });
    }
  } else {
    res.status(405).json({ message: 'Method Not Allowed' });
  }
}
